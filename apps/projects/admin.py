# apps/projects/admin.py
from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')  # id will show UUID
    readonly_fields = ('id',)  # make UUID read-only in admin form
