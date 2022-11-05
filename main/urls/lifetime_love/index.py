from django.urls import path, re_path
from main.views.lifetime_love.literature_view import LiteratureView


urlpatterns = [

    path('literature/', LiteratureView.as_view(), name="myspace_user"),
    # re_path(r".*", index, name="myspace_index"),
]