from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    # classdetails = models.ManyToManyField(Classdetail, related_name="classdetails")


class Classdetail(models.Model):
    name = models.CharField(max_length=60)
    categories = models.ManyToManyField(Category, related_name="categories")
    type = models.CharField(max_length=60, default="")
    tags = models.TextField(default="")
    blurb = models.TextField(default="")
    lat = models.DecimalField(max_digits=18, decimal_places=15, default=0.0)
    lng = models.DecimalField(max_digits=18, decimal_places=15, default=0.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
