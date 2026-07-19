from django.contrib import admin
from .models import LoisirCategorie, LoisirItem


class LoisirItemInline(admin.TabularInline):
    model = LoisirItem
    extra = 1
    fields = ['title', 'description', 'image', 'ordering']


@admin.register(LoisirCategorie)
class LoisirCategorieAdmin(admin.ModelAdmin):
    list_display = ['title', 'ordering']
    ordering = ['ordering']
    inlines = [LoisirItemInline]


@admin.register(LoisirItem)
class LoisirItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'categorie', 'ordering']
    list_filter = ['categorie']
    ordering = ['categorie', 'ordering']