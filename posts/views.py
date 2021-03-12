from django.views.generic.base import TemplateView
from .models import Post

class HomePageView(TemplateView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'nombre_correos'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContentPageView(TemplateView):
    template_name = 'content.html'
