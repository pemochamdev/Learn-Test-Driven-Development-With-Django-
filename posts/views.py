from django.shortcuts import render

# Create your views here.
from posts.models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, "posts/home.html", context)
