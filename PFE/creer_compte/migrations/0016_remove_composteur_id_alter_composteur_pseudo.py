# Generated by Django 4.1.7 on 2023-04-30 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creer_compte', '0015_greener_composteur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composteur',
            name='id',
        ),
        migrations.AlterField(
            model_name='composteur',
            name='pseudo',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
