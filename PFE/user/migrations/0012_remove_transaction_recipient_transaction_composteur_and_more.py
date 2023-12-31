# Generated by Django 4.1.7 on 2023-05-01 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creer_compte', '0023_remove_greener_id_alter_greener_pseudo'),
        ('user', '0011_transaction_valider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='recipient',
        ),
        migrations.AddField(
            model_name='transaction',
            name='composteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='creer_compte.composteur'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='greeneur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='creer_compte.greener'),
        ),
    ]
