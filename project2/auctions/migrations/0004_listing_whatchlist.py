# Generated by Django 3.0 on 2023-05-27 19:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20230526_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='whatchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='listingWhatchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
