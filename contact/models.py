from django.db import models

# Create your models here.
class contact(models.Model):
    ContactID=models.AutoField(primary_key=True)
    FullName=models.CharField(max_length=100, null=False)
    Email=models.CharField(max_length=100, null=False)
    Mobile_No=models.CharField(max_length=20, null=False)
    Location=models.CharField(max_length=100, null=False)
    Message=models.CharField(max_length=500, null=False)

class requestbook(models.Model):
    RequestID=models.AutoField(primary_key=True)
    ISBN_No=models.CharField(max_length=100, null=False)
    BookTitle=models.CharField(max_length=100, null=False)
    AuthorName=models.CharField(max_length=100, null=False)
    Quantity=models.IntegerField(null=False)
    EmailID=models.CharField(max_length=100, null=False)
    Mobile_No=models.CharField(max_length=20, null=False)
  