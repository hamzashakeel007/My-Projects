# Generated by Django 5.0.3 on 2024-04-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]