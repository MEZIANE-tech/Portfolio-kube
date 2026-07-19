from django.contrib import admin
from django.urls import path
from Blog.views import BlogIndexView, blog_detail,  CommandeUtileIndexView, commandes_utiles_detail, tutoriels_list, tutoriel_detail



urlpatterns = [
    path('', BlogIndexView.as_view(), name='Blog'),
    path('commandes-utiles/', CommandeUtileIndexView.as_view(), name='commandes_utiles_index'),
    path('commandes-utiles/<slug:slug>/', commandes_utiles_detail, name='commandes_utiles_detail'),
    path('tutoriels/', tutoriels_list, name='tutoriels_list'),
    path('tutoriels/<slug:slug>/', tutoriel_detail, name='tutoriel_detail'),
    path('<slug:slug>/', blog_detail, name='blog_detail'),

]
