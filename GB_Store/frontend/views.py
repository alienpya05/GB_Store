from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import backend.models as model

# Create your views here.

def Accueil(request):
    return render(request,'accueil.html')


def Produit(request):
    categories = model.Categorie.objects.all()
    return render(request, 'produit.html', {'categories': categories})
 
def Ventes(request):
    return render(request, 'ventes.html')

def Dashboard(request):
    return render(request, 'dashboard.html')

def CategorieForm(request):
    return render(request,'addCategorie.html')

def AddCategorie(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        image = request.FILES.get('image')  # Assurez-vous d'utiliser request.FILES pour les fichiers téléchargés

        # Création d'une nouvelle instance de Categorie avec les données reçues du formulaire
        nouvelle_categorie = model.Categorie.objects.create(
            nomCategorie=nom,
            description=description,
            image=image
        )

        # Sauvegarde de la nouvelle catégorie
        nouvelle_categorie.save()

        # Redirection vers une page de confirmation ou toute autre page souhaitée après l'ajout
        return redirect('Produits')

    return render(request, 'votre_template.html')  

def Categorie(request, categorie_id):
    # Récupérer la catégorie correspondant à l'identifiant fourni
    categorie = get_object_or_404(model.Categorie, pk=categorie_id)

    # Passer la catégorie récupérée au template pour l'affichage des détails
    return render(request, 'categories.html', {'categorie': categorie})


def ArticleForms(request):
    categories = model.Categorie.objects.all()
    promotions = model.Promotion.objects.all()
    return render(request, 'addArticle.html', {'categories': categories, 'promotions': promotions})

def AddArticle(request):
    if request.method == 'POST':
        nom_article = request.POST.get('nomArticle')
        prix = request.POST.get('prix')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')
        disponibilite = request.POST.get('disponibilite')

        # Vérification de la disponibilité
        disponibilite = True if disponibilite == 'on' else False

        promotion_id = request.POST.get('promotion')
        categorie_id = request.POST.get('categorie')

        # Récupération de la promotion et de la catégorie sélectionnées
        promotion = None
        categorie = None

        # Vérification des valeurs vides pour l'ID de la promotion et de la catégorie
        if promotion_id:
            try:
                promotion = model.Promotion.objects.get(id=promotion_id)
            except model.Promotion.DoesNotExist:
                pass

        if categorie_id:
            try:
                categorie = model.Categorie.objects.get(id=categorie_id)
            except model.Categorie.DoesNotExist:
                pass

        # Création d'une nouvelle instance de l'article avec les données reçues du formulaire
        nouvel_article = model.Article.objects.create(
            nomArticle=nom_article,
            prix=prix,
            stock=stock,
            image=image,
            disponibilite=disponibilite,
            promotion=promotion,
            categorie=categorie
        )

        # Sauvegarde du nouvel article
        nouvel_article.save()

        # Redirection vers une page de confirmation ou toute autre page souhaitée après l'ajout
        return redirect('Produits')  # Remplacez 'categories.html' par l'URL de votre choix

    return render(request, 'addArticle.html')  # Renvoyer un rendu si la méthode HTTP n'est pas POST