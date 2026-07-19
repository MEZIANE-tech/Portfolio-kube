from django.contrib import admin
from .models import CV, HeroSection, AboutSection, Competence

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ['mis_a_jour_le']
    
@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['titre', 'sous_titre']
 
    def has_add_permission(self, request):
        # Empêche de créer plus d'un Hero
        if HeroSection.objects.exists():
            return False
        return True

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['__str__']
 
    def has_add_permission(self, request):
        if AboutSection.objects.exists():
            return False
        return True
 
 
@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ['titre', 'niveau', 'ordering']
    ordering = ['ordering']