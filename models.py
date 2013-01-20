from django.db import models

# Create your models here.
class User(models.Model):
  pass_md5 = models.CharField(max_length=50) # MD5 function for password
  empire_name = models.CharField(max_length=50) # Name of empire
  population = models.IntegerField() # Population number
  reg_date = models.DateField() # Registration date
  left_right_pointer = models.FloatField()
  