from django.shortcuts import render
from .serializers import TweetSerializer, TweetActionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Tweet
from user.models import User



@api_view(["POST"])
def create_tweet(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.data)
    dummy = User.objects.all().first()
    if serializer.is_valid():
        # serializer.save(user=request.user)
        serializer.save(user=dummy)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])

def list_tweet(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def detail_tweet(request, tweet_id,*args, **kwargs):
    try:
        tweet = Tweet.objects.filter(id=tweet_id)
    except Tweet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TweetSerializer(tweet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = TweetSerializer(tweet, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        tweet.delete()
        return Response(status=status.HTTP_200_OK)


def tweet_action_view(request,*args, **kwargs):
    serializer = TweetActionSerializer(data = request.POST)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get('id')
        action = data.get('action')

        tweet = Tweet.objects.filter(id=tweet_id)
        if not tweet.exists():
            return Response(status=status.HTTP_404_NOT_FOUND) 
        tweet = tweet.first()
        if action == "like":
            tweet.likes.add(request.user)
            serializer = TweetSerializer(tweet)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif action == "unlike":
            tweet.likes.remove(request.user)
        elif action == "retweet":
            pass

    return Response({"message":"Tweet Removed"}, status=status.HTTP_200_OK)
