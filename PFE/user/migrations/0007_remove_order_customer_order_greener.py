# Generated by Django 4.1.7 on 2023-04-12 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_order_image_remove_order_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='greener',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
