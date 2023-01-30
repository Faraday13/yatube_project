from django.urls import path

from .views import index, group_posts


urlpatterns = [
    path('', index),
    path('groups/<slug:slug>', group_posts),
]
