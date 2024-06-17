from django.db import models

# Create your models here.
class users(models.Model):
    UserID=models.AutoField(primary_key=True)
    UserType=models.CharField(max_length=100, default='customer')
    CompanyName=models.CharField(max_length=100, null=False,default='NA')
    CompanyLocation=models.CharField(max_length=100,null=False,default='NA')
    GST_No=models.IntegerField(null=False,default=0)
    FirstName=models.CharField(max_length=100,null=False,default='NA')
    LastName=models.CharField(max_length=100,null=False,default='NA')
    Username=models.CharField(max_length=100,null=False,unique=True)
    Password=models.CharField(max_length=100,null=False)
    Mobile_No=models.CharField(max_length=20,null=False,unique=True)
    Address=models.CharField(max_length=100, null=False,default='NA')
    Zipcode=models.IntegerField(null=False)



