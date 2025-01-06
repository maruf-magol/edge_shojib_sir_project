from django.db import models

# Create your models here.

class Base(models.Model):
    name = models.CharField(max_length=30)

class User(models.Model):
    name = models.CharField(max_length=30)
    roll = models.BigIntegerField()

    def __str__(self):
        return f"{self.name} - {self.roll}"