from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)

  def __str__(self) -> str:
    return self.name


