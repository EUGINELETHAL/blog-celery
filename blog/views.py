from django.views import generic
from django.shortcuts import render
from .models import Post,Comment


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def get_comments(request, pk):
    post = Post.objects.get(pk=pk)
    comments=Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }
    return render(request, "comment.html", context)

