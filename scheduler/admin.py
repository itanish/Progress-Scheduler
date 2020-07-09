from django.contrib import admin
from .models import user_project, project_module, project_task

# Register your models here.
admin.site.register(user_project)
admin.site.register(project_module)
admin.site.register(project_task)
