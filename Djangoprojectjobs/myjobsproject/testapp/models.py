from django.db import models
# Create your models here.
class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
class BngJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=60)
    eligibility = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

