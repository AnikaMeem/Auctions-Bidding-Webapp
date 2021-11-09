# Generated by Django 3.2.9 on 2021-11-08 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_watchlist_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='watchlist_users',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
