from django.contrib import admin
from .models import Tweet, TweetLike


class TweetLikeAdmin(admin.TabularInline):
    """Tabular Inline View for TweetLike"""

    model = TweetLike


class TweetAdmin(admin.ModelAdmin):
    inlines = [TweetLikeAdmin]
    list_display = ["__str__", "user"]
    search_fields = ["content", "user__email", "user__handle"]

    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetAdmin)
