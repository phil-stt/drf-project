from django.contrib import admin
# from watchlist_app.models import Movie
from watchlist_app.models import WatchList, StreamPlatform, Review
#from watchlist_app.models import Gig, GigReview

# Register your models here.
# admin.site.register(Movie)
admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
# admin.site.register(Gig)
# admin.site.register(GigReview)