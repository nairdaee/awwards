from django.contrib import admin
from .models import Project, Profile, Rating, technologies, categories

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('technologies', 'categories')

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Rating)
admin.site.register(categories)
admin.site.register(technologies)
