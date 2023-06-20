# Generated by Django 4.1.7 on 2023-04-12 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creer_compte', '0012_alter_composteur_image_alter_greener_image'),
        ('user', '0004_remove_orderitem_order_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('points', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='creer_compte.greener')),
            ],
        ),
    ]