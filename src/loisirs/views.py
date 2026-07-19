from django.shortcuts import render
from .models import LoisirCategorie


def loisirs_view(request):
    categories = LoisirCategorie.objects.prefetch_related('items').all()
    return render(request, 'loisirs/loisirs.html', {'categories': categories})