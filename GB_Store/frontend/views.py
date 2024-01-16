from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
import backend.models as model
from django import forms
from decimal import Decimal
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


def Categorie_Formulaire(request):
    return render(request,'addCategorie.html')


def Ajouter_Categorie(request):
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

    return render(request, 'rien.html')  


def Categorie(request, categorie_id):
    # Récupérer la catégorie correspondant à l'identifiant fourni
    categorie = get_object_or_404(model.Categorie, pk=categorie_id)
    # Passer la catégorie récupérée au template pour l'affichage des détails
    return render(request, 'categories.html', {'categorie': categorie})


def modifier_categorie(request, categorie_id):
    categorie = get_object_or_404(model.Categorie, id=categorie_id)

    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        categorie.nomCategorie = nom
        categorie.description = description

        if image:
            categorie.image = image

        categorie.save()
        return redirect('Produits')  

    
    context = {'categorie': categorie}
    return render(request, 'modifierCategorie.html', context)


def supprimer_categorie(request, categorie_id):
    categorie = get_object_or_404(model.Categorie, id=categorie_id)

    if request.method == 'POST':
        categorie.delete()
        return redirect('Produits') 

    return render(request, 'confirmation-suppression-categorie.html', {'categorie': categorie})


def confirmation_suppression_categorie(request, categorie_id):
    categorie = get_object_or_404(model.Categorie, id=categorie_id)
    return render(request, 'confirmation-suppression-categorie.html', {'categorie': categorie})


def Article_Formulaire(request):
    categories = model.Categorie.objects.all()
    promotions = model.Promotion.objects.all()
    return render(request, 'addArticle.html', {'categories': categories, 'promotions': promotions})


def Article(request, article_id):
    
    article = get_object_or_404(model.Article, pk=article_id)
    return render(request, 'article.html', {'article': article})



def Modifier_Article(request, article_id):
    article = get_object_or_404(model.Article, id=article_id)

    if request.method == 'POST':
        article.nomArticle = request.POST.get('nomArticle')
        article.prix = request.POST.get('prix')
        article.stock = request.POST.get('stock')
        article.disponible = request.POST.get('disponible') == 'on'

        image = request.FILES.get('image')
        if image:
            article.image = image

        promotion_id = request.POST.get('promotion')
        categorie_id = request.POST.get('categorie')
        if promotion_id:
            try:
                article.promotion = model.Promotion.objects.get(id=promotion_id)
            except model.Promotion.DoesNotExist:
                return HttpResponse("Promotion non trouvée.", status=404)
        else:
            # Si promotion_id n'est pas défini, assurez-vous que l'article n'a pas de promotion
            article.promotion = None

        try:
            article.categorie = model.Categorie.objects.get(id=categorie_id)
        except model.Categorie.DoesNotExist:
            return HttpResponse("Catégorie non trouvée.", status=404)

        article.save()
        return redirect('Article', article_id=article.id)
    else:
        # Chargez les données existantes dans le contexte pour les afficher dans le formulaire
        context = {
            'article': article,
            'promotions': model.Promotion.objects.all(),
            'categories': model.Categorie.objects.all(),
        }
        return render(request, 'modifierArticle.html', context)

def supprimer_Article(request, article_id):
    article = get_object_or_404(model.Article, id=article_id)

    if request.method == 'POST':
        article.delete()
        return redirect('Produits')

    return render(request, 'accueil.html', {'article': article})


def confirmation_suppression_Article(request, article_id):
    article = get_object_or_404(model.Article, id=article_id)

    if request.method == 'POST':
        article.delete()
        return redirect('Categorie')

    return render(request, 'confirmation-suppression.html', {'article': article})


def Ajouter_Article(request):
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
            disponible=disponibilite,
            promotion=promotion,
            categorie=categorie
        )

        # Sauvegarde du nouvel article
        nouvel_article.save()

        return redirect('Produits')  

    return render(request, 'addArticle.html')  

def ajouter_au_panier(request):
    if request.method == 'POST':
        article_id = request.POST.get('article_id')
        quantity = int(request.POST.get('quantity', 1))

        try:
            article = get_object_or_404(model.Article, id=article_id)
        except model.Article.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Article non trouvé.'})

        # Assurez-vous que la session_id est correctement définie
        if not request.session.session_key:
            request.session.save()

        # Obtenir ou créer le panier basé sur la session_id
        panier, _ = model.Panier.objects.get_or_create(session_id=request.session.session_key)

        # Obtenir ou créer la relation ArticlePanier
        article_panier, created = model.ArticlePanier.objects.get_or_create(
            panier=panier,
            article=article,
            defaults={'quantite': quantity}
        )

        if not created:
            article_panier.quantite += quantity
            article_panier.save()

        # Calculer le prix total par article
        prix_total_article = article.prix * quantity

       
        return JsonResponse({
            'success': True,
            'message': 'Article ajouté au panier avec succès.',
            'prix_total_article': prix_total_article,
        })

    return JsonResponse({'success': False, 'message': 'Méthode non autorisée.'})
def afficher_panier(request):
    # Assurez-vous que la session est correctement définie
    request.session.setdefault("session_key", request.session.session_key)
    
    # Obtenez le panier basé sur la session
    panier, _ = model.Panier.objects.get_or_create(session_id=request.session.session_key)
    
    # Obtenez tous les articles du panier
    articles_du_panier = model.ArticlePanier.objects.filter(panier=panier)
    
    # Calculer le prix total du panier
    prix_total_panier = sum(item.article.prix * item.quantite for item in articles_du_panier)

    # Calculer le prix total par article dans le panier
    prix_total_article = {item.article.id: item.article.prix * item.quantite for item in articles_du_panier}
    
    # Ajouter le prix total par article à chaque article_panier
    for item in articles_du_panier:
        item.prix_total_article = prix_total_article.get(item.article.id, 0)
    
    # Passez les données au template
    context = {
        'articles_du_panier': articles_du_panier,
        'prix_total_panier': prix_total_panier,
    }

    return render(request, 'afficherPanier.html', context)

def formulaireVente(request):

    # Obtenez le panier basé sur la session
    panier, _ = model.Panier.objects.get_or_create(session_id=request.session.session_key)
    
    # Obtenez tous les articles du panier
    articles_du_panier = model.ArticlePanier.objects.filter(panier=panier)
    
    # Calculer le prix total du panier
    prix_total_panier = sum(item.article.prix * item.quantite for item in articles_du_panier)
    
    return render (request,'formulaireVente.html',{'prix_total_panier' : prix_total_panier})

def vendre(request):
    if request.method == 'POST':
        montant_total = request.POST.get('montant_facture')
        montant_paye = request.POST.get('somme_payee')
        #Calcule du montant à rendre

        montant_rendu = max(Decimal(0), float(montant_paye) - float(montant_total))
        # Création de la vente
        vente = model.Vente.objects.create(
            montant_total=montant_total,
            montant_paye=montant_paye,
            montant_rendu=montant_rendu
        )

        # Récupération des articles du panier
        articles_panier = model.ArticlePanier.objects.all()

        for article_panier in articles_panier:
            # Création de l'ArticleVente associé à la vente en cours
            model.ArticleVente.objects.create(
                article=article_panier.article,
                vente=vente,
                quantite_vendue=article_panier.quantite
            )
             # Soustration de la quantité vendue du stock de l'article
            article = article_panier.article
            article.stock -= article_panier.quantite
            article.save()
            
            #changement du status à indisponible
            if article.stock == 0:
                article.disponible = False
                article.save()

        model.ArticlePanier.objects.all().delete()

        # Suppression du panier lui-même
        panier = model.Panier.objects.get(session_id=request.session.session_key)
        panier.delete()
        return redirect(Accueil)

    else:
        # Afficher le formulaire vide pour la première fois

        # Récupération des articles du panier
        articles_panier = model.ArticlePanier.objects.all()

        context = {
            'articles_panier': articles_panier,
        }

        return render(request, 'vendre.html', context)
    
def rechercher_Article(request):
    search_query = request.GET.get('search', '')

    # Recherche dans la base de données
    results = model.Article.objects.filter(nomArticle__icontains=search_query)
    return render(request, 'resultat-recherche.html', {'results': results, 'search_query': search_query})