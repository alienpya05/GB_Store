"""
URL configuration for GB_Store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('Accueil/',views.Accueil,name="Acceuil"),
    path('Produits/',views.Produit,name="Produits"),
    path('Ventes/', views.Ventes, name='Ventes'),
    path('Vashboard/', views.Dashboard, name='Dashboard'),
    path('CategorieForm/',views.CategorieForm,name='CategorieForm'),
    path('AddCategorie/', views.AddCategorie, name="AddCategorie"), 
    path('ArticleForms/',views.ArticleForms,name='ArticleForms'),
    path('AddArticle/', views.AddArticle, name="AddArticle"),
    path('Categorie/<int:categorie_id>/', views.Categorie, name='Categorie'),
   
]