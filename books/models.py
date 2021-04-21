from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)


# 3shan fi admin y7ot title el book bdl obj 1 w hakza
    def __str__(self):          
        return self.title