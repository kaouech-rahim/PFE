# Generated by Django 4.1.7 on 2023-04-30 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creer_compte', '0014_greener_quantite'),
    ]

    operations = [
        migrations.AddField(
            model_name='greener',
            name='composteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='creer_compte.composteur'),
        ),
    ]