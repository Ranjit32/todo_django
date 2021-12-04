from datetime import timezone
from django.db import models
from django.utils import timezone


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=150)
    isCompleted = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.title}"

    
