from django.views.generic import TemplateView
from .models import Post

class HomePageView(TemplateView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'superlista'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContentPageView(TemplateView):
    template_name = 'content.html'
