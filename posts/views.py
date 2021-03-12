from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'superlista'

class AboutPageView(ListView):
    template_name = 'about.html'

class ContentPageView(ListView):
    template_name = 'content.html'
    model = Post
    context_object_name = 'superlista'
