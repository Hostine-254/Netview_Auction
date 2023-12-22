from django.db import models
from datetime import datetime,date
from django.db.models.fields import (DateTimeField,DurationField,DateField,TimeField,EmailField,)
# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=25)
    profile=models.ImageField(upload_to='pics')
    img1=models.ImageField(upload_to='pics' ,null=True, blank=True )
    img2=models.ImageField(upload_to='pics' ,null=True, blank=True )
    img3=models.ImageField(upload_to='pics' ,null=True, blank=True )
    img4=models.ImageField(upload_to='pics' ,null=True, blank=True )
    condition=models.CharField(null=True,max_length=15)
    short_description=models.CharField(max_length=150)
    long_description=models.TextField()
    discount=models.IntegerField(null=True)
    basePrice=models.IntegerField()
    currentPrice=models.IntegerField()
    
    tag=models.CharField(max_length=25)
    
    status=models.CharField(null=True,max_length=25)
    
    sold=models.CharField(max_length=10,default="unsold")
    
    ownermail = models.EmailField(unique=False)
    start_date=models.DateField()
    highest_bidder=models.IntegerField(null=True)

    sendwinmail = models.CharField(max_length=7,default="unsended")
    @property
    def imageURL(self):
        try:
            url = self.img1
        except:
            url=''
        return url
    @property
    def imageURL(self):
        try:
            url = self.img2
        except:
            url=''
        return url
    @property
    def imageURL(self):
        try:
            url = self.img3
        except:
            url=''
        return url
    @property
    def imageURL(self):
        try:
            url = self.img4
        except:
            url=''
        return url