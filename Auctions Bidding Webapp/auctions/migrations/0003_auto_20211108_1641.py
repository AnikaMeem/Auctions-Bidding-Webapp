# Generated by Django 3.2.9 on 2021-11-08 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20211108_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
