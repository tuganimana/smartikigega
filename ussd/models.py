from django.db import models

# Create your models here.
class Farmers(models.Model):
    firstname= models.CharField(max_length=255,default='')
    lastname= models.CharField(max_length=255,default='')
    gender = models.CharField(max_length=255,default='')
    district = models.CharField(max_length=255,default='')
    village = models.CharField(max_length=255,default='')
    email = models.CharField(max_length=255,default='')
    country = models.CharField(max_length=255,default='')
    harvesttype = models.CharField(max_length=255,default='')
    dateofbirth = models.CharField(max_length=255,default='')
    number = models.CharField(max_length=255,default='')
    Cooperative=models.CharField(max_length=255,default='')
    code=models.CharField(max_length=255,default='')
    pincode=models.CharField(max_length=255,default='')
    sector=models.CharField(max_length=255,default='') 
    cell=models.CharField(max_length=255,default='') 
    def __str__(self):
        return self.firstname 