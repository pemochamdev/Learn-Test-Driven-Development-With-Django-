from django.urls import path

from posts import views

urlpatterns = [
    path("", views.index, name="home"),
    path("post/<post_id>/", views.post_detail, name="post_detail"),
]
