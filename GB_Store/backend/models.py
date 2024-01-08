from django.db import models

# Create your models here.

class Categorie(models.Model):
    nomCategorie = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

class Article(models.Model):
    nomArticle = models.CharField(max_length=100)
    prix = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    disponibilite = models.BooleanField(default=True)
    promotion = models.ForeignKey('Promotion', on_delete=models.SET_NULL, null=True, blank=True)
    date_debut_promotion = models.DateField(null=True, blank=True)
    date_fin_promotion = models.DateField(null=True, blank=True)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

class Promotion(models.Model):
    nomPromotion = models.CharField(max_length=100)
    typePromotion = models.CharField(max_length=100)
    valeurPromotion = models.FloatField()

class Achat(models.Model):
    date_achat = models.DateTimeField(auto_now_add=True)
    montant_paye = models.FloatField()
    articles = models.ManyToManyField(Article, through='AchatArticle')

class AchatArticle(models.Model):
    achat = models.ForeignKey('Achat', on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    quantite = models.IntegerField()