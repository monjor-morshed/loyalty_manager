# Generated by Django 5.1.4 on 2024-12-22 16:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_customer_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoyaltyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('points', models.PositiveIntegerField(default=0)),
                ('members', models.ManyToManyField(related_name='loyalty_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
