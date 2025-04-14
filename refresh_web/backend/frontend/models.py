from django.db import models 

class review_Models(models.Model):
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    phone= models.IntegerField()
    review= models.CharField(max_length=255)