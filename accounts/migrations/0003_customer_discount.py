# Generated by Django 5.1.4 on 2024-12-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customer_individual_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='discount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
