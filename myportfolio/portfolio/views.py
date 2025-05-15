from django.shortcuts import render
from .models import Education, Technology, Achievement, Project


def home(request):
    education = Education.objects.first()
    technologies = Technology.objects.all()
    achievements = Achievement.objects.all()
    projects = Project.objects.all()

    tech_categories = {
        'backend': technologies.filter(category='backend'),
        'frontend': technologies.filter(category='frontend'),
        'database': technologies.filter(category='database'),
        'devops': technologies.filter(category='devops'),
        'ds': technologies.filter(category='ds'),
    }

    context = {
        'education': education,
        'tech_categories': tech_categories,
        'achievements': achievements,
        'projects': projects,
    }

    return render(request, 'portfolio/home.html', context)