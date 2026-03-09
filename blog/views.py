from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-create_time')
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context=context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context=context)