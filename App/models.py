from django.db import models
class Account_Details(models.Model):
    First_Name = models.CharField(max_length = 30)
    Last_Name = models.CharField(max_length = 30)
    Emails = models.CharField(max_length = 30)
    Contac_no = models.IntegerField(12)
    Address = models.TextField()
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    