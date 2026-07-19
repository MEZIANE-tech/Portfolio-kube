from django.shortcuts import render, get_object_or_404
from Blog.models import BlogSection, CommandeUtile, Tutoriel
from django.views.generic import View, TemplateView, ListView
from django.http import Http404
from django.template import TemplateDoesNotExist
# Create your views here.



class BlogIndexView(ListView):
    model = BlogSection
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    
    def get_queryset(self):
        # Filtrer les expériences où published = True
        return BlogSection.objects.filter(published=True)

def blog_detail(request, slug):
    try:
        return render(request, f'blog/{slug}.html')
    except TemplateDoesNotExist:
        raise Http404("Page non trouvée")
    
    

class CommandeUtileIndexView(ListView):
    model = CommandeUtile
    template_name = 'blog/commandes-utiles/commandes-utiles.html'
    context_object_name = 'sections'
    
    def get_queryset(self):
        return CommandeUtile.objects.filter(published=True)
    
    
def commandes_utiles_detail(request, slug): 
    section = get_object_or_404(CommandeUtile, slug=slug, published=True) 
    return render(request, 'blog/commandes-utiles/detail-commandes-utiles.html', {'section': section})


def tutoriels_list(request):
    tutoriels = Tutoriel.objects.filter(published=True).order_by('-last_updated')
    return render(request, 'blog/tutoriels/tutoriels.html', {'tutoriels': tutoriels})

def tutoriel_detail(request, slug): 
    tutoriel = get_object_or_404(Tutoriel, slug=slug, published=True) 
    return render(request, 'blog/tutoriels/detail-tutoriels.html', {'tutoriel': tutoriel})