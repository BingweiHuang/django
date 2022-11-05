from django.contrib import admin
from main.models.player.player import Player
from main.models.myspace.follow import Follow
from main.models.myspace.post import Post

from main.models.lifetime_love.models import Literature
from main.models.lifetime_love.models import Figure
from main.models.lifetime_love.models import FigureCategory
from main.models.lifetime_love.models import Category

# Register your models here.

admin.site.register(Player)
admin.site.register(Follow)
admin.site.register(Post)

admin.site.register(Literature)
admin.site.register(Figure)
admin.site.register(FigureCategory)
admin.site.register(Category)
