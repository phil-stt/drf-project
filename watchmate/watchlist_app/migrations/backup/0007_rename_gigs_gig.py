# Generated by Django 3.2.15 on 2022-09-23 20:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watchlist_app', '0006_rename_reviews_gigreview'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gigs',
            new_name='Gig',
        ),
    ]