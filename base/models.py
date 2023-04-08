from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ToDoItem(models.Model):
      
    STATUS_CHOICES = ( ("W", "Waiting"), ("P", "In Progress"), ("D", "Done" ))
    PRIORITY_CHOICES = ( ( 1, "High"), (2, "Medium"), (3, "Low" ))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='W')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)

    def __str__(self):
        return self.name

    





