# Generated by Django 4.1.7 on 2023-04-12 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='image',
        ),
        migrations.RemoveField(
            model_name='order',
            name='points',
        ),
    ]
