# Generated by Django 4.1.6 on 2023-02-15 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creer_compte', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cominauteur',
            old_name='Nom_utilisateur',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='composteur',
            old_name='Nom_utilisateur',
            new_name='username',
        ),
    ]