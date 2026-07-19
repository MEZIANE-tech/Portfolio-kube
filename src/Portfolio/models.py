from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os


class CV(models.Model):
    fichier = models.FileField(upload_to='documents/', verbose_name="Fichier CV (PDF)")
    mis_a_jour_le = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "CV"

    def __str__(self):
        return f"CV — {self.mis_a_jour_le.strftime('%d/%m/%Y')}"


@receiver(post_delete, sender=CV)
def supprimer_fichier_cv(sender, instance, **kwargs):
    if instance.fichier and os.path.isfile(instance.fichier.path):
        os.remove(instance.fichier.path)


class HeroSection(models.Model):
    titre = models.CharField(max_length=200, verbose_name="Titre (ex: Ingénieur Systèmes...)")
    sous_titre = models.CharField(max_length=200, verbose_name="Sous-titre (ex: Fiabilité, Résilience...)")
    presentation = models.TextField(verbose_name="Texte de présentation")
    photo = models.ImageField(upload_to='hero/', verbose_name="Photo de profil")
 
    class Meta:
        verbose_name = "Section Hero"
 
    def __str__(self):
        return f"Hero — {self.titre}"
 
 
@receiver(post_delete, sender=HeroSection)
def supprimer_photo_hero(sender, instance, **kwargs):
    if instance.photo and os.path.isfile(instance.photo.path):
        os.remove(instance.photo.path)
 
 
@receiver(pre_save, sender=HeroSection)
def supprimer_ancienne_photo_hero(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        ancienne = HeroSection.objects.get(pk=instance.pk)
    except HeroSection.DoesNotExist:
        return
 
    if ancienne.photo and instance.photo and ancienne.photo != instance.photo:
        if os.path.isfile(ancienne.photo.path):
            os.remove(ancienne.photo.path)
 
    if ancienne.photo and not instance.photo:
        if os.path.isfile(ancienne.photo.path):
            os.remove(ancienne.photo.path)

class AboutSection(models.Model):
    paragraphe_1 = models.TextField(verbose_name="Paragraphe 1")
    paragraphe_2 = models.TextField(verbose_name="Paragraphe 2", blank=True, null=True)
    paragraphe_3 = models.TextField(verbose_name="Paragraphe 3", blank=True, null=True)
 
    class Meta:
        verbose_name = "Section À propos"
 
    def __str__(self):
        return "Section À propos"
 
 
class Competence(models.Model):
    titre = models.CharField(max_length=100, verbose_name="Titre")
    niveau = models.PositiveIntegerField(
        verbose_name="Niveau (1 à 5)",
        default=3,
        choices=[(i, str(i)) for i in range(1, 6)]
    )
    ordering = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")
 
    class Meta:
        ordering = ['ordering']
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"
 
    def __str__(self):
        return self.titre