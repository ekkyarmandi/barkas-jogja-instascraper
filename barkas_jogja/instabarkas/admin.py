from django.contrib import admin

from .models import Post, PostSideCard, PostOwner, ProfileAnalytic

admin.site.register(Post)
admin.site.register(PostSideCard)
admin.site.register(PostOwner)
admin.site.register(ProfileAnalytic)