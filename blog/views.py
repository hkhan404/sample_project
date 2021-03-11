from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

class PostListView(ListView):
	model = Post
	queryset = Post.objects.all()
	context_object_name = "posts"
	template_name = "blog/post_list.html"


class PostDetailView(DetailView):
	model = Post
	template_name = "blog/post_detail.html"
	context_object_name = "post"