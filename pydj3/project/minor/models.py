from django.db import models

# Create your models here.
class user(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    phno=models.CharField(max_length=15)
    subject=models.CharField(max_length=100)
    class Meta:
        db_table="user"
        
class user2(models.Model):
    email=models.EmailField()
    pwd=models.CharField(max_length=50)
    class Meta:
        db_table="user2"