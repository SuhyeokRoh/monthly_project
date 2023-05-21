from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.serializers import ReviewListSerializer, CommentListSerializer
from movies.models import Movie


class UserSignupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "email", "nickname",)


class UserSerializer(serializers.ModelSerializer):
    
    class MovieTitleSerailizer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ("title",)
    
    review_set = ReviewListSerializer(many=True, read_only=True)
    like_reviews = ReviewListSerializer(many=True, read_only=True)
    movielike = MovieTitleSerailizer(many=True, read_only=True)
    comment_set = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = "__all__"
        
# 팔로우
class FollowSerializer(serializers.ModelSerializer):

    class UserfollowSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username','followings')

    followers = UserfollowSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'followings', 'followers')