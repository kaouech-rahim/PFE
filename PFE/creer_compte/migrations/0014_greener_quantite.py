# Generated by Django 4.1.7 on 2023-04-27 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creer_compte', '0013_greener_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='greener',
            name='quantite',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]