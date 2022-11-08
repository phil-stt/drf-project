from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Below for function based views
# from watchlist_app.api.views import movie_list, movie_details
# from watchlist_app.api.views import MovieListAV, MovieDetailAV
from watchlist_app.api import views

# from .views import ReviewsCreateAPI

router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')
#router.register('stream', views.StreamPlatformVS.as_view({'get': 'list'}), basename='streamplatform')

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-detail'),
    path('list2/', views.WatchListGV.as_view(), name='watch-list'),
    # Removed below for Router
    #path('stream/', views.StreamPlatformAV.as_view(), name='stream'),
    #path('stream/<int:pk>', views.StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    # Using Router below
    path('', include(router.urls)),
    #path('stream/<int:pk>/review', views.StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    path('<int:pk>/reviews', views.ReviewList.as_view(), name='review-list'),
    path('<int:pk>/reviews/create', views.ReviewCreate.as_view(), name='review-create'),
    #path('review/', views.ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review-detail'),
    path('user-reviews/', views.UserReview.as_view(), name='user-review-detail')
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

