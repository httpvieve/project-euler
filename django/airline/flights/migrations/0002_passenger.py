# Generated by Django 4.2.13 on 2024-09-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Passenger",
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
                ("first_name", models.CharField(max_length=64)),
                ("last_name", models.CharField(max_length=64)),
                (
                    "flights",
                    models.ManyToManyField(
                        blank=True, related_name="passenger", to="flights.flight"
                    ),
                ),
            ],
        ),
    ]
