from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    return render(request, 'poemssproj/index.html')

def article(request, post_id):
    post= get_object_or_404(Post, pk= post_id)
    context= {
        'post': post
    }
    return render(request, 'poemssproj/article.html', context)

def poem(request):
    context= {
        'posts': Post.objects.all().order_by('-date_posted')
    }
    return render(request, 'poemssproj/poem.html', context)

def blog(request):
    return render(request, 'poemssproj/blog.html')

def lifestyle(request):
    return render(request, 'poemssproj/lifestyle.html')

def story(request):
    return render(request, 'poemssproj/story.html')


