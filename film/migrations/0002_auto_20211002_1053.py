# Generated by Django 3.2.7 on 2021-10-02 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='actor_id',
            new_name='actors',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='movie_id',
        ),
    ]