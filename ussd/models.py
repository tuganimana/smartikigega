from django.db import models

# Create your models here.
class Farmers(models.Model):
    firstname= models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    harvesttype = models.CharField(max_length=255)
    dateofbirth = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    Cooperative=models.CharField(max_length=255,default='')
    code=models.CharField(max_length=255)
    pincode=models.CharField(max_length=255)
    sector=models.CharField(max_length=255) 
    cell=models.CharField(max_length=255) 
    def __str__(self):
        return self.firstname 