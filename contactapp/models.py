from django.db import models


class ContactData(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    company = models.CharField(max_length=20)
    salary = models.IntegerField()
    location = models.CharField(max_length=15)
