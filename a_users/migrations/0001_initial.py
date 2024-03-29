# Generated by Django 5.0.1 on 2024-01-24 18:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("realname", models.CharField(blank=True, max_length=20, null=True)),
                ("email", models.EmailField(max_length=254, null=True, unique=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("nationality", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "campermode",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Hammock", "Hammock"),
                            ("Small Tent", "Small Tent"),
                            ("Large Tent", "Large tent"),
                            ("Car", "Car"),
                            ("Van", "Van"),
                            ("CamperVan", "CamperVan"),
                            ("Motorhome", "Motorhome"),
                            ("Small Caravan", "Small Caravan"),
                            ("Large Caravan", "Large Caravan"),
                            ("Trailer Tent", "Trailer Tent"),
                            ("Cabin/Mobile Home", "Cabin/Mobile Home"),
                            ("Under the Stars", "Under the Stars"),
                        ],
                        default="Hammock",
                        max_length=20,
                        null=True,
                    ),
                ),
                ("camperstory", models.TextField(blank=True, null=True)),
                (
                    "fav_campsite",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "level",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("SC_Founder1", "SuperCamper Founder1"),
                            ("SC_Founder2", "SuperCamper Founder2"),
                            ("New_SuperCamper", "New SuperCamper"),
                            ("SuperCamper", "SuperCamper"),
                            ("SuperCamper Expert", "SuperCamper Expert"),
                            ("SuperCamper Master", "SuperCamper Master"),
                            ("Restricted SuperCamper", "Restricted SuperCamper"),
                            ("Banned", "Banned"),
                        ],
                        default="New SuperCamper",
                        max_length=30,
                        null=True,
                    ),
                ),
                ("plot_reports", models.IntegerField(blank=True, default=0, null=True)),
                ("numplots", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
