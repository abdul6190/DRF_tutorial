from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=3)
    
    def __str__(self):
        return f'Employee_{self.name}'
    