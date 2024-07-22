from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Institution(models.Model):
    FUND = 'fundacja'
    ORG = 'organizacja porządkowa'
    ZBIÓR = 'zbiórka lokalna'

    TYPES = {
        (FUND, 'fundacja'),
        (ORG, 'organizacja porządkowa'),
        (ZBIÓR, 'zbiórka lokalna')
    }
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(choices=TYPES, max_length=100, default=FUND)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ManyToManyField(Institution)
    adress = models.TextField()
    phone_number = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.TextField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(null=True, default='brak komentarza')
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
