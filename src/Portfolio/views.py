from datetime import datetime, date
from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
import os
from django.conf import settings
from django.views.generic import View, TemplateView, ListView
from cv.models import Experience, Formation
from .models import CV, HeroSection, AboutSection, Competence


class IndexView(ListView):
    model = Experience
    template_name = 'Portfolio/index.html'
    context_object_name = 'experiences'

    def get_queryset(self):
        return Experience.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        experiences = Experience.objects.filter(published=True)
        certifications = Formation.objects.filter(certification=True)

        parcours = []

        for exp in experiences:
            parcours.append({
                'type': 'experience',
                'year': exp.start_date.year,
                'data': exp
            })

        for cert in certifications:
            parcours.append({
                'type': 'certification',
                'year': int(cert.year),
                'data': cert
            })

        parcours.sort(key=lambda item: item['year'])

        context['parcours'] = parcours
        context['hero'] = HeroSection.objects.first()  
        context['about'] = AboutSection.objects.first()
        context['competences'] = Competence.objects.all()

        return context
    
        
    
def redirect_to_experience(request, slug):
    # Vérifier que le slug existe dans le modèle Experience
    experience = get_object_or_404(Experience, slug=slug)
    
    # Rediriger vers la page cible avec l'ID correspondant au slug
    return redirect(f'/cv#{experience.slug}')



def download_cv(request):
    cv = CV.objects.last()  # prend le dernier CV uploadé
    if cv and cv.fichier:
        return FileResponse(cv.fichier.open('rb'), as_attachment=True, filename='Yacine_MEZIANE_CV.pdf')
    raise Http404("CV non trouvé")
    
    
def coming_soon(request):
    return render(request, "common/coming-soon.html")

def health(request):
    return HttpResponse("OK")


