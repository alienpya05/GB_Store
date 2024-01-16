from django.db import models

class Categorie(models.Model):
    nomCategorie = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    promotion = models.ForeignKey('Promotion', on_delete=models.SET_NULL, null=True, blank=True)

class Promotion(models.Model):
    nomPromotion = models.CharField(max_length=100)
    typePromotion = models.CharField(max_length=100)
    valeurPromotion = models.DecimalField(max_digits=10, decimal_places=2)
    date_debut_promotion = models.DateField()
    date_fin_promotion = models.DateField()

class Article(models.Model):
    nomArticle = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    promotion = models.ForeignKey(Promotion, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images/')

class Panier(models.Model):
    session_id = models.CharField(max_length=50)
    articles = models.ManyToManyField('Article', through='ArticlePanier')

class ArticlePanier(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    panier = models.ForeignKey('Panier', on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    

class Vente(models.Model):
    articles = models.ManyToManyField('Article', through='ArticleVente')
    date_vente = models.DateTimeField(auto_now_add=True)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2)
    montant_rendu = models.DecimalField(max_digits=10, decimal_places=2)

class ArticleVente(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    vente = models.ForeignKey('Vente', on_delete=models.CASCADE)
    quantite_vendue = models.PositiveIntegerField()
