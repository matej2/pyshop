# Generated by Django 3.0.5 on 2020-04-27 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.Offer'),
        ),
    ]
