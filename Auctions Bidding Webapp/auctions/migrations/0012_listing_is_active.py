# Generated by Django 3.2.9 on 2021-11-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20211108_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
