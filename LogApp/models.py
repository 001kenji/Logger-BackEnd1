from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100,null=True)
    
    email = models.EmailField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    def _str_(self):
        return f"{self.name}{self.email}"