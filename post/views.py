from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return  render(request,"posts/post_list.html",
                   {"posts":posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post_page.html",
                  {"post": post})