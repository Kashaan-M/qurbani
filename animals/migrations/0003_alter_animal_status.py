# Generated by Django 4.2.20 on 2025-05-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("animals", "0002_animal_photo_1_animal_photo_2_animal_photo_3_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="status",
            field=models.CharField(
                choices=[("s", "بک گیا"), ("a", "دستیاب"), ("u", "دستیاب نہیں ہے")],
                default="a",
                max_length=1,
            ),
        ),
    ]
