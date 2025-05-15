from django.db import models


class Education(models.Model):
    degree = models.CharField(max_length=100)
    description = models.TextField()
    years = models.CharField(max_length=50)

    def __str__(self):
        return self.degree


class Technology(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('database', 'Database'),
        ('devops', 'DevOps'),
        ('ds', 'Data Science'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    level = models.CharField(max_length=100)
    years_exp = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.title