from wsgiref.validate import validator
from rest_framework import serializers
#from watchlist_app.models import Movie
from watchlist_app.models import WatchList, StreamPlatform, Review
#from watchlist_app.models import Gig, GigReview

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')
    average_rating = serializers.SerializerMethodField()
    def get_average_rating(self, obj):
        return obj.average_rating

    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    #watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail'
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"

# class MovieSerializer(serializers.ModelSerializer):
#     len_name = serializers.SerializerMethodField()
    
    
#     class Meta:
#         model = Movie
#         # exclude = ('watchlist',)
#         fields = "__all__"
#         # fields = ['name']

# Custom method to create a calculated field not in model
    # def get_len_name(self, object):
    #     length = len(object.name)
    #     return length

    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name is required to be diff than description")
    #     else:
    #         return data
            
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value

#Regular Serializer
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
# # Object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name is required to be diff than description")
#         else:
#             return data
            
# # Field level validation example
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#         else:
#             return value
    
# class GigSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Gig
#         fields = ['id','title','price','details','seller','images']

#Working below for Gig exp
# class GigSerializer (serializers.ModelSerializer):
#     average_rating = serializers.SerializerMethodField()
#     def get_average_rating(self, obj):
#         return obj.average_rating
#     class Meta:
#         model = Gig
#         fields = ['id','title','price','details','seller','images','average_rating']

# class GigReviewSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = GigReview
#         fields = ['id','rating','comment','item','buyer','created_at']
    

