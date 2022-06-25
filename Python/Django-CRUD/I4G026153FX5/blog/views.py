from dataclasses import fields
from django.views import generic
from pdb import post_mortem
from django.shortcuts import render
from django.urls import reverse_lazy


from blog.models import Post


# Create your views here.

class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"

class PostCreateView(generic.CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

