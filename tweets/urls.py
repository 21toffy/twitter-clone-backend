from django.urls import path
from . import views

app_name = "listings"
# realtor_listings
urlpatterns = [
    path("post/tweet", views.create_tweet),
    path("tweets/list", views.list_tweet),
    path("tweet/detail/<int:tweet_id>", views.detail_tweet),
    path("tweet/delete/<int:tweet_id>", views.detail_tweet),
    path("tweet/action/", views.tweet_action_view),
]
