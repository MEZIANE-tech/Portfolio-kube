from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your models here.
# Modèle pour le projet
class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    slug = models.SlugField(max_length=100, blank=True)
    description = models.TextField(verbose_name="Description")
    tasks = models.TextField(verbose_name="Taches")
    icon = models.CharField(max_length=50, verbose_name="Icône", help_text="Ex: fas fa-gears", blank=True, null=True)
    ordering = models.IntegerField(default=0, verbose_name="Ordre")
    published = models.BooleanField(default=False, verbose_name="Publié")

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.title)}"
        super().save(*args, **kwargs)
    
    
    
    
class Experience(models.Model):
    poste = models.CharField(max_length=255, verbose_name="Poste")
    slug = models.SlugField(max_length=100, blank=True)
    entreprise = models.CharField(max_length=255, verbose_name="Entreprise", blank=True, null=True)
    description = models.TextField(blank=True)
    projects = models.ManyToManyField(Project, blank=True, verbose_name="Projets")  # Champ ManyToMany
    last_updated = models.DateTimeField(auto_now=True)
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    image_name = models.CharField(max_length=100, blank=True, null=True)
    icon_name = models.CharField(max_length=100, blank=True, null=True)
    
    
    class Meta:
        ordering = ['-start_date']
        verbose_name = "Experience"

    def __str__(self):
        return f"{self.poste} ({self.start_date.year})"
    
    def save(self, *args, **kwargs):
        year = self.start_date.year
        self.slug = f"{slugify(self.poste)}-{year}"
        super().save(*args, **kwargs)
        
        
        
        
class Formation(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    slug = models.SlugField(max_length=100, blank=True)
    institution = models.CharField(max_length=255, verbose_name="Institution", null=True, blank=True)
    certification = models.BooleanField(default=False, verbose_name="Certification")
    published = models.BooleanField(default=False, verbose_name="Publié")
    year = models.IntegerField(default=2024, verbose_name="Année")
    link = models.URLField(max_length=255, blank=True, null=True, verbose_name="Lien")
    icon_name = models.CharField(max_length=100, blank=True, null=True)
    
    
    def clean(self):
        if self.year:
            if self.year < 1000 or self.year > 2200:
                raise ValidationError(f"L'année {self.year} n'est pas valide. Elle doit être comprise entre 1000 et 2200.")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-year']
        verbose_name = "Formation"
    
    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.title)}-{self.year}"
        super().save(*args, **kwargs)
    

class Competence(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    slug = models.SlugField(max_length=100, blank=True)
    image_name = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(verbose_name="Contenu")
    identifier = models.IntegerField(default=999, verbose_name="Identifiant")

    def __str__(self):
        return self.title

    
    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.title)}"
        super().save(*args, **kwargs)
        
        
