from django.contrib import admin
from .models import Education, Technology, Achievement, Project

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level')
    list_filter = ('category',)

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('technologies',)

admin.site.register(Education)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Achievement)
admin.site.register(Project, ProjectAdmin)