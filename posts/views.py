from django.shortcuts import render, redirect

# Create your views here.


from posts.models import Post
from posts.forms import PostCreationForm


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, "posts/home.html", context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {
        'post':post,
    }
    return render(request, 'posts/detail.html', context)


def post_creation(request):
    template_name = 'posts/post_creation.html'

    form = PostCreationForm()
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('home')



    context = {
        'form':form,
    }
    return render(request, template_name, context)