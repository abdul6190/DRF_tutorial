from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = PhoneNumberField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class Order(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.product    
