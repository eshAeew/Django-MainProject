# Generated by Django 5.1.2 on 2025-02-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='story_covers/'),
        ),
    ]
