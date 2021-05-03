from rest_framework import serializers
from .models import Tweet


TWEET_ACTION_OPTIONS = ['like', 'unlike', 'retweet']
class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    def validate_action(self, value):
        value = value.lower().strip()
        if not value in TWEET_ACTION_OPTIONS:
            raise validationError("This is not a valid option")
        return value


class TweetSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Tweet
        fields=['id', 'content', 'likes']
    def get_likes(self, obj):
        return obj.likes.count()
            
    def validate_content(self, value):
        if len(value)>240:
            raise serializers.validationError('this Tweet is too long')
        return value