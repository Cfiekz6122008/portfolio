from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Project, Skill


def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'portfolio/home.html', {
        'projects': projects,
        'skills': skills,
        'form': form
    })