# Generated by Django 3.1.3 on 2020-11-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0008_remove_profile_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
