from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
  name = models.CharField(max_length=255, null=True)
  email = models.CharField(max_length=255)

  def __str__(self) -> str:
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=255, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  digital = models.BooleanField(default=False, null=True, blank=False)
  image = models.ImageField(null=True, blank=True)
  
  @property
  def imageUrl(self):
    imageUrl = self.image.url
    try: 
      url = imageUrl
    except: 
      url = ''
    return url

  def __str__(self) -> str:
    return self.name

class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
  date_ordered = models.DateTimeField(auto_now_add=True)
  complete = models.BooleanField(default=False, null=True, blank=False)
  transaction_id = models.CharField(max_length=100, null=True)

  def __str__(self) -> str:
    return str(self.id)

class OrderItem(models.Model):
  quantity = models.IntegerField()
  date_added = models.DateTimeField(auto_now_add=True)
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)

class ShippingAddress(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
  address = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=255)
  zipcode = models.CharField(max_length=255)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return self.address
