from django.contrib import admin
from .models import user_project, project_module, project_task, pre_launch_email, slot_left

# Register your models here.
admin.site.register(user_project)
admin.site.register(project_module)
admin.site.register(project_task)
admin.site.register(pre_launch_email)
admin.site.register(slot_left)
