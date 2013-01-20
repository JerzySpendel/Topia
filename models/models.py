from django.db import models
# Create your models here.
class User(models.Model):
  login = models.CharField(max_length=25)
  activated = models.BooleanField()
  pass_md5 = models.CharField(max_length=50) # MD5 function for password
  empire_name = models.CharField(max_length=50) # Name of empire
  population = models.IntegerField() # Population number
  reg_date = models.DateTimeField() # Registration date
  money = models.IntegerField()
  pop_money = models.IntegerField()
  last_act = models.FloatField()
  tax = models.IntegerField()
class Town(models.Model):
  name = models.CharField(max_length=20)
  population = models.IntegerField()
class Activation(models.Model):
  usr = models.ForeignKey(User)
  code = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
class Research(models.Model):
  name = models.CharField(max_length=20)
  level = models.IntegerField()
  cost = models.IntegerField()
  owner = models.ForeignKey(User)