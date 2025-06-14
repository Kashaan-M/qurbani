# Generated by Django 4.2.20 on 2025-05-31 10:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("animals", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="photo_1",
            field=models.ImageField(default="animal.png", upload_to="uploads/"),
        ),
        migrations.AddField(
            model_name="animal",
            name="photo_2",
            field=models.ImageField(
                blank=True, default="animal.png", upload_to="uploads/"
            ),
        ),
        migrations.AddField(
            model_name="animal",
            name="photo_3",
            field=models.ImageField(
                blank=True, default="animal.png", upload_to="uploads/"
            ),
        ),
        migrations.AddField(
            model_name="animal",
            name="photo_4",
            field=models.ImageField(
                blank=True, default="animal.png", upload_to="uploads/"
            ),
        ),
        migrations.AddField(
            model_name="animal",
            name="photo_5",
            field=models.ImageField(
                blank=True, default="animal.png", upload_to="uploads/"
            ),
        ),
        migrations.AlterField(
            model_name="owner",
            name="photo",
            field=models.ImageField(default="person.png", upload_to="uploads/"),
        ),
    ]
