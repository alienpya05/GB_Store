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
    path('CategorieForm/',views.Categorie_Formulaire,name='CategorieForm'),
    path('AddCategorie/', views.Ajouter_Categorie, name="AddCategorie"), 
    path('ArticleForms/',views.Article_Formulaire,name='ArticleForms'),
    path('AddArticle/', views.Ajouter_Article, name="AddArticle"),
    path('Categorie/<int:categorie_id>/', views.Categorie, name='Categorie'),
    path('article/<int:article_id>/', views.Article, name='Article'),
    path('modifier_article/<int:article_id>/', views.Modifier_Article, name='modifier_article'),
    path('supprimer_article/<int:article_id>/', views.supprimer_Article, name='supprimer_article'),
    path('confirmation-suppression-article/<int:article_id>/confirm/',views.confirmation_suppression_Article, name='confirmation_suppression'),
    path('modifier_categorie/<int:categorie_id>/', views.modifier_categorie, name='modifier_categorie'),
    path('confirmation_suppression_categorie/<int:categorie_id>/', views.confirmation_suppression_categorie, name='confirmation_suppression_categorie'),
    path('supprimer_categorie/<int:categorie_id>/', views.supprimer_categorie, name='supprimer_categorie'),
    path('ajouter-au-panier/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('afficher_panier/', views.afficher_panier, name='afficher_panier'),
    path('formulaireVente/',views.formulaireVente,name='formulaireVente'),
    path('vendre/',views.vendre,name="vendre"),
    path('rechercherArticle/',views.rechercher_Article,name="rechercher_Article")
]