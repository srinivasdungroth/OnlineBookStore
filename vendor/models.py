from django.db import models
from customer.models import users



# Create your models here.
class books(models.Model):
    BookID = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to='static/images')
    CategoryName = models.CharField(max_length=100, null=False)
    BookTitle = models.CharField(max_length=100, null=False)
    AuthorName = models.CharField(max_length=100, null=False)
    ISBN = models.CharField(max_length=20, null=False, default='NA')
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    CutPrice = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    QuantityAvailable = models.IntegerField(null=False)
    BindingType = models.CharField(max_length=20, choices=[('PAPERBACK','paperback'),('HARDCOVER','hardcover')], default='PAPERBACK')
    vendorID = models.ForeignKey(users, on_delete=models.CASCADE)
    SoldBy = models.CharField(max_length=100, null=False)

#orders table
class orders(models.Model):
    OrderId=models.AutoField(primary_key=True)
    UserId=models.ForeignKey(users,on_delete=models.CASCADE)
    SoldBy=models.CharField(max_length=100,null=False)
    SoldTo=models.CharField(max_length=100,null=False)
    BookId=models.ForeignKey(books,on_delete=models.CASCADE)
    BookName=models.CharField(max_length=100,null=False)
    Quantity=models.IntegerField(default=1)
    UnitPrice=models.DecimalField(max_digits=10,decimal_places=2,null=False)
    TotalAmount=models.DecimalField(max_digits=10,decimal_places=2,null=False)
    OrderDate=models.DateField(null=False)
    DeliveryDate=models.DateField(null=False)
    OrderStatus=models.CharField(max_length=10,choices=[('PENDING','pending'),('SHIPPING','shipping'),('DELIVERED','delivered')],default='PENDING')
    PaymentStatus=models.CharField(max_length=10,choices=[('PAID','paid'),('PENDING','pending')],default='PENDING')
    Mobile_No=models.IntegerField(null=False,unique=True)
    Address=models.CharField(max_length=100,null=False)
    ZipCode=models.IntegerField(null=False)
    