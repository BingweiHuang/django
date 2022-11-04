from django.contrib import admin
from main.models.player.player import Player
from main.models.myspace.follow import Follow
from main.models.myspace.post import Post

# Register your models here.

admin.site.register(Player)
admin.site.register(Follow)
admin.site.register(Post)
