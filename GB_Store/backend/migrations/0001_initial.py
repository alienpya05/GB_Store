# Generated by Django 5.0 on 2024-01-08 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_achat', models.DateTimeField(auto_now_add=True)),
                ('montant_paye', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomArticle', models.CharField(max_length=100)),
                ('prix', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('disponibilite', models.BooleanField(default=True)),
                ('date_debut_promotion', models.DateField(blank=True, null=True)),
                ('date_fin_promotion', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCategorie', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomPromotion', models.CharField(max_length=100)),
                ('typePromotion', models.CharField(max_length=100)),
                ('valeurPromotion', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='AchatArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('achat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.achat')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
            ],
        ),
        migrations.AddField(
            model_name='achat',
            name='articles',
            field=models.ManyToManyField(through='backend.AchatArticle', to='backend.article'),
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.categorie'),
        ),
        migrations.AddField(
            model_name='article',
            name='promotion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.promotion'),
        ),
    ]
