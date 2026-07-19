"""
URL configuration for Portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from Portfolio.views import IndexView, download_cv, coming_soon, redirect_to_experience, health
from django.conf import settings
from django.conf.urls.static import static


SOCIAL_LINKS = {
    'facebook': 'https://www.facebook.com/YACINExMEZIANE',
    'twitter':  'https://x.com/MEZIANEDYacine',
    'linkedin': 'https://www.linkedin.com/in/yacine-meziane-613325313/',
    'github':   'https://github.com/MEZIANE-tech',
}

urlpatterns = [
    path("health/", health),
    path('', IndexView.as_view(), name="Portfolio"),
    path('cv/', include("cv.urls")),
    path('admin/', admin.site.urls),
    path('redirect/<slug:slug>/', redirect_to_experience, name='redirect-to-experience'),
    path('download-cv/', download_cv, name='download-cv'),
    path('contact/', include("Contact.urls")),
    path('coming-soon/', coming_soon, name='coming-soon'),
    path('loisirs/', include('loisirs.urls')),
    path('blog/', include("Blog.urls")),

    *[
        path(f'{name}/', RedirectView.as_view(url=url, permanent=False), name=name)
        for name, url in SOCIAL_LINKS.items()
    ],
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

