# Generated by Django 4.1.7 on 2023-06-07 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creer_compte', '0032_delete_greener_greeneur_pseudo_c'),
    ]

    operations = [
        migrations.AddField(
            model_name='composteur',
            name='lat',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='composteur',
            name='lng',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='greeneur',
            name='lat',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='greeneur',
            name='lng',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
