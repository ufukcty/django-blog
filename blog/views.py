from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def index_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "home.html", {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post.html", {'post':post})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return index_page(request)


def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})