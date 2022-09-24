from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework import mixins

# from watchlist_app.models import Gig,GigReview
# from .serializers import GigSerializer,GigReviewSerializer

from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework import viewsets

# from rest_framework.mixins import ListModelMixin, CreateModelMixin , RetrieveModelMixin , DestroyModelMixin, UpdateModelMixin
# from rest_framework.permissions import AllowAny
from django.db.models import Avg

from watchlist_app.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
 
# from watchlist_app.models import Movie
from watchlist_app.models import WatchList, StreamPlatform, Review
# from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.api.serializers import (WatchListSerializer, 
                                           StreamPlatformSerializer, 
                                           ReviewSerializer)

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")

        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2
        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()
        
        serializer.save(watchlist=watchlist, review_user=review_user)
    

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]    

    
# Class based views with generics and mixins
# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    #permission_classes = [IsAdminOrReadOnly]
    #throttle_classes = [AnonRateThrottle]

# class StreamPlatformVS(viewsets.ViewSet):

#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist, context={'request': request})
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

class StreamPlatformAV(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]

    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(
            platform, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):
    #permission_classes = [IsAdminOrReadOnly]
    #throttle_classes = [AnonRateThrottle]
    def get_queryset(self):
        return WatchList.objects.all().annotate(_average_rating=Avg('reviews__rating')) 

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    #permission_classes = [IsAdminOrReadOnly]
    #throttle_classes = [AnonRateThrottle]

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Demo versions
# class MovieListAV(APIView):
    
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
# class MovieDetailAV(APIView):
    
#     def get(self, request, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
        
#     def put(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
# Function based views below
# @api_view(['GET', 'POST'])
# def movie_list(request):
    
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'POST'])
# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):

#     if request.method == 'GET':

#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#List and create (pk not required)
# class GigsListAPI(GenericAPIView, ListModelMixin ):
#     def get_queryset(self):
#        username = self.kwargs['user']
#        return Gig.objects.filter(seller=username)
#     serializer_class = GigSerializer
#     permission_classes = (AllowAny,)

#     def get(self, request , *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class GigsListCategorywise(GenericAPIView, ListModelMixin ):
#     def get_queryset(self):
#        SearchedCategory = self.kwargs['category']
#        return Gigs.objects.filter(category=SearchedCategory)
#     serializer_class = GigsSerializer
#     permission_classes = (AllowAny,)

#     def get(self, request , *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# Working below Gigs Exp
# class GigsListAll(GenericAPIView, ListModelMixin ):
#     queryset = Gig.objects.all()
#     serializer_class = GigSerializer
#     permission_classes = (AllowAny,)

#     # def get_queryset(self):

#     #     return Gig.objects.all().annotate(_average_rating=Avg('reviews__rating')

#     def get(self, request , *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class GigsListAll(ListModelMixin, GenericAPIView): 
#     serializer_class = GigSerializer
#     permission_classes = (AllowAny,)

#     def get_queryset(self):
#         return Gig.objects.all().annotate(_average_rating=Avg('gigreviews__rating')) 
    
#     def get(self, request , *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
# class GigsCreateAPI(GenericAPIView, CreateModelMixin):
#     queryset = Gig.objects.all()
#     serializer_class = GigSerializer
#     permission_classes = (AllowAny,)

#     def post(self, request , *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# # Retrieve, update and delete (pk required)
# class RUDGigsAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin,  DestroyModelMixin):
#     queryset = Gig.objects.all()
#     serializer_class = GigSerializer
#     permission_classes = (AllowAny,)

#     def get(self, request , *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request , *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def put(self, request , *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
    
#     def delete(self, request , *args, **kwargs): 
#         pk = kwargs.get('pk')
#         p = Gig.objects.get(id=pk)
#         if p.images:
#             p.images.delete() 
#         return self.destroy(request, *args, **kwargs)



# # VIEWS FOR REVIEWS MODEL
# class GigReviewListAPI(GenericAPIView, ListModelMixin ):
#     def get_queryset(self):
#         # pk = self.kwargs['pk']
#         # return GigReview.objects.filter(item=pk)
#         item = self.kwargs['item']
#         return GigReview.objects.filter(item=item)
#     #    return GigReview.objects.all()
#     serializer_class = GigReviewSerializer
#     permission_classes = (AllowAny,)

#     def get(self, request , *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class ReviewsCreateAPI(GenericAPIView, CreateModelMixin):
#     queryset = GigReview.objects.all()
#     serializer_class = GigReviewSerializer
#     permission_classes = (AllowAny,)

#     def post(self, request , *args, **kwargs):
#         return self.create(request, *args, **kwargs)  