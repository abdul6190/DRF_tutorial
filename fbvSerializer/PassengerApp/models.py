from django.db import models

# Create your models here.

class Passenger(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    travelPoints = models.IntegerField()
    
    def __str__(self):
        return f'{self.firstName} {self.lastName}'
