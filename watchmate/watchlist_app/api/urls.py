from django.urls import path, include
# Below for function based views
# from watchlist_app.api.views import movie_list, movie_details
# from watchlist_app.api.views import MovieListAV, MovieDetailAV
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail')
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

