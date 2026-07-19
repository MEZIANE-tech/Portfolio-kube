from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView
from cv.models import Experience, Formation, Competence, Project
# Create your views here.



def cv(request):
    return redirect('/coming_soon/')

# class CvView(ListView):
#     model = Experience
#     template_name = 'cv/cv.html'
#     context_object_name = 'experiences'
    
#     def get_queryset(self):
#         # Filtrer les expériences où published = True
#         return Experience.objects.filter(published=True)



class CvView(TemplateView):
    template_name = 'cv/cv.html'
    
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiences'] = Experience.objects.filter(published=True)
        context['diplomes'] = Formation.objects.filter(published=True, certification=False)
        context['certifications'] = Formation.objects.filter(published=True, certification=True)
        context['competences'] = Competence.objects.all().order_by('identifier')
        return context


