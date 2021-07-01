from django.shortcuts import render
from .models import Posts
from django.views.generic import (CreateView)
from django.urls import reverse

class PostCreateView(CreateView):
    model = Posts
    template_name = "blog/post_form.html"
    fields = ["author", "title", "content"]
    
    
    def get_success_url(self):
        return reverse('blog-home')

def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
