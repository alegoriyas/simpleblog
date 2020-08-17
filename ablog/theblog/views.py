from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

#def home(request):
    #return render(request, 'theblog/home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'theblog/home.html'
    #ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'theblog/article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'theblog/add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'theblog/update_post.html'
    #fields = ['title', 'title_tag', 'author', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    success_url = reverse_lazy('home')