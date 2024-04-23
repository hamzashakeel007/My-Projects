# Generated by Django 5.0.3 on 2024-03-31 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing_comment_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='current_price',
            field=models.FloatField(default=models.FloatField()),
        ),
        migrations.AlterField(
            model_name='listing',
            name='starting_bid',
            field=models.FloatField(),
        ),
    ]