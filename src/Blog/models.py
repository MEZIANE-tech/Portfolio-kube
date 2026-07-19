from django.db import models
from django.utils.text import slugify
# Create your models here.



class BlogSection(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titre")  # Ex: "Commandes utiles"
    slug = models.SlugField(unique=True, blank=True)                # Ex: "commandes-utiles"
    emoji = models.CharField(max_length=50, blank=True)             # Ex: "💻"
    description = models.TextField()                                # Ex: "Toutes les commandes essentielles Unix, GPG, Git..."
    last_updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False, verbose_name="Publié")

    def __str__(self):
        return f"{self.emoji} {self.title}"

    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.title)}"
        super().save(*args, **kwargs)
        
    
class CommandeUtile(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titre")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField() 
    last_updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(verbose_name="Contenu", null=True, blank=True)

    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.title)}"
        super().save(*args, **kwargs)



class Tutoriel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titre")
    slug = models.SlugField(unique=True, blank=True, max_length=150)
    description = models.TextField() 
    last_updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(verbose_name="Contenu", null=True, blank=True)

    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.title)}"
        super().save(*args, **kwargs)


