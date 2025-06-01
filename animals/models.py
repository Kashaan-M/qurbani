from sys import maxsize
from django.db import models
import uuid

# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    village = models.CharField(max_length=200)
    city = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=100)
    photo = models.ImageField(default="person.png", upload_to="uploads/")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Animal(models.Model):
    ANIMAL_CATEGORY = (
        ('b','Bakra'),
        ('d','Dumba'),
        ('v','Vehra'),
        ('c','Camel'),
        )
    ANIMAL_STATUS = (
        ('s','بک گیا'),
        ('a','دستیاب'),
        ('u','دستیاب نہیں ہے'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this animal")
    breed = models.CharField(max_length=200)
    age = models.CharField(max_length=2)
    gender = models.CharField(choices=(('m','Male'),('f','Female')), max_length=1, default='m')
    location = models.CharField(max_length=100, default="Bhatta Chowk, Rawalpindi", blank=True)
    quoted_price = models.CharField(max_length=7)
    defects = models.CharField(max_length=300, default="No", blank=True)
    teeth = models.CharField(max_length=10)
    weight = models.CharField(max_length=20, default="1", blank=True)
    category = models.CharField(choices=ANIMAL_CATEGORY, default="b", max_length=1)
    status = models.CharField(choices=ANIMAL_STATUS, default="a", max_length=1)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    photo_1 = models.ImageField(default="animal.png", upload_to="uploads/")
    photo_2 = models.ImageField(default="animal.png", upload_to="uploads/", blank=True)
    photo_3 = models.ImageField(default="animal.png", upload_to="uploads/", blank=True)
    photo_4 = models.ImageField(default="animal.png", upload_to="uploads/", blank=True)
    photo_5 = models.ImageField(default="animal.png", upload_to="uploads/", blank=True)
    create_date = models.DateTimeField(auto_now_add= True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.breed} -{self.owner}"