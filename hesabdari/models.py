from django.db import models

# Create your models here.
class Income(models.Model):
    personID = models.IntegerField( null=False )
    amount = models.IntegerField()
    title = models.CharField(max_length=50)
    Date = models.DateField(auto_now=False, auto_now_add=False , null = True )