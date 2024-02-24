# Generated by Django 5.0.1 on 2024-02-24 14:35

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_users", "0004_alter_profile_realname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=django_resized.forms.ResizedImageField(
                blank=True,
                crop=None,
                force_format=None,
                keep_meta=True,
                null=True,
                quality=85,
                scale=None,
                size=[600, 600],
                upload_to="images/",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="realname",
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
