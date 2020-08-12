from django.shortcuts import render
from django.views.generic import ListView, DetailView


#def home(request):
    #return render(request, 'theblog/home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'theblog/home.html'