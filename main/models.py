from django.db import models

# Create your models here.


class MultiStepFormModel(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    twitter=models.CharField(max_length=255)
    facebook=models.CharField(max_length=255)
    gplus=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

    def __str__(self):
        return self.fname