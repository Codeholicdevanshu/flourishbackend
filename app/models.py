from django.db import models

# Create your models here.

class Country(models.Model):
    #id = models.BigAutoField(primary_key=True)
    date_id = models.CharField(max_length=19)
    generation = models.CharField(max_length=30)
    value = models.CharField(max_length=20)
    def __str__(self):
        return self.generation

