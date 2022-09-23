from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Below for function based views
# from watchlist_app.api.views import movie_list, movie_details
# from watchlist_app.api.views import MovieListAV, MovieDetailAV
from watchlist_app.api.views import (WatchListAV, WatchDetailAV, 
                                     StreamPlatformAV, StreamPlatformDetailAV, 
                                     ReviewCreate, ReviewList, ReviewDetail,
                                     StreamPlatformVS)

# from .views import GigsListAll, GigReviewListAPI, RUDGigsAPI, ReviewsCreateAPI

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')
#router.register('stream', StreamPlatformVS.as_view({'get': 'list'}), basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    # Removed below for Router
    #path('stream/', StreamPlatformAV.as_view(), name='stream'),
    #path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    # Using Router below
    path('', include(router.urls)),
    #path('stream/<int:pk>/review', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    path('<int:pk>/reviews', ReviewList.as_view(), name='review-list'),
    path('<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    #path('review/', ReviewList.as_view(), name='review-list'),
    #path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    # path('gigs/', GigsListAll.as_view(), name='gigs-list-all'),
    # path('gigs/<int:pk>', RUDGigsAPI.as_view(), name='gig-detail'),
    # path('gigs/<int:item>/reviews/', GigReviewListAPI.as_view(), name='gig-review-list'),
    # path('gigs/<int:pk>/createreview/', ReviewsCreateAPI.as_view(), name='gig-review-create')
]

# Below for function based views
# urlpatterns = [
#     path('list/', movie_list, name='movie-list'),
#     path('<int:pk>', movie_details, name='movie-detail'),
# ]

# urlpatterns = [
#     path('list/', MovieListAV.as_view(), name='movie-list'),
#     path('<int:pk>', MovieDetailAV.as_view(), name='movie-detail'),
# ]

