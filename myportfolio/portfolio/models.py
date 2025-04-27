from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"