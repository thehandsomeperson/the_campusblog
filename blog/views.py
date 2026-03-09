from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-create_time')
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context=context)