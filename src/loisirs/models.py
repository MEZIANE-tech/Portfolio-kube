from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os


class LoisirCategorie(models.Model):
    """
    Catégorie de loisir (ex: Animes, Jeux vidéo, Sport...)
    """
    title = models.CharField(max_length=100, verbose_name="Titre")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    icon = models.CharField(
        max_length=100,
        verbose_name="Icône FontAwesome",
        help_text="Ex: fa-solid fa-gamepad",
        default="fa-solid fa-star"
    )
    ordering = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        ordering = ['ordering']
        verbose_name = "Catégorie de loisir"
        verbose_name_plural = "Catégories de loisirs"

    def __str__(self):
        return self.title


class LoisirItem(models.Model):
    """
    Item dans une catégorie (ex: Attack on Titan, Zelda...)
    """
    categorie = models.ForeignKey(
        LoisirCategorie,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Catégorie"
    )
    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    image = models.ImageField(
        upload_to='loisirs/',
        verbose_name="Image",
        blank=True,
        null=True
    )
    ordering = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        ordering = ['ordering']
        verbose_name = "Item de loisir"
        verbose_name_plural = "Items de loisirs"

    def __str__(self):
        return f"{self.categorie.title} — {self.title}"
    
@receiver(post_delete, sender=LoisirItem)
def supprimer_image_loisir(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)
        
@receiver(pre_save, sender=LoisirItem)
def supprimer_ancienne_image(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        ancienne = LoisirItem.objects.get(pk=instance.pk)
    except LoisirItem.DoesNotExist:
        return
    
    # Cas 1 : image remplacée par une nouvelle
    if ancienne.image and instance.image and ancienne.image != instance.image:
        if os.path.isfile(ancienne.image.path):
            os.remove(ancienne.image.path)
    
    # Cas 2 : image effacée (cochée "Effacer" dans l'admin)
    if ancienne.image and not instance.image:
        if os.path.isfile(ancienne.image.path):
            os.remove(ancienne.image.path)