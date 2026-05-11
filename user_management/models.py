from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100,primary_key=True,db_index=True)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    
    def __str__(self):
        return f"{self.name}"