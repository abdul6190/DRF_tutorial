from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    ratings = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    
    def __str__(self):
        return self.name