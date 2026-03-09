from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import CreatePostForm
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

@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if 'save_draft' in request.POST:
                post.status = 'draft'
            else:
                post.status = 'published'
            post.save()
            return redirect('blog:post_list')

    else:
        form = CreatePostForm()
    return render(request, 'blog/create_post.html', context={'form': form})
