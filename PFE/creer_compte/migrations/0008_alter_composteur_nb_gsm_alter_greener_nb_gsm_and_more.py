# Generated by Django 4.1.7 on 2023-03-13 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creer_compte', '0007_greener_delete_cominauteur_remove_composteur_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composteur',
            name='NB_GSM',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='greener',
            name='NB_GSM',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='greener',
            name='nom',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='greener',
            name='prenom',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='greener',
            name='pseudo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
