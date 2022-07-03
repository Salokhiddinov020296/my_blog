from django.shortcuts import render
from django.views.generic import ListView

from blogs.models import BlogsModel


class BlogsView(ListView):
    model = BlogsModel
    template_name = 'main/post.html'
