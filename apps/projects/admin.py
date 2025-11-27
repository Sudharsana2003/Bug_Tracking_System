# apps/projects/admin.py
from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'description',
        'created_by',
        'created_at'
    )

    readonly_fields = ('id', 'created_at')

    search_fields = ('name', 'description')
    ordering = ('-created_at',)

    list_filter = (
        'created_at',
        'created_by'
    )

    #  PERMISSION CONTROL
    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists()

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists()

    # AUTO SET CREATED BY
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
