from django.db import models
from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
from django.utils import timezone
import random 
import string
from datetime import datetime    

STATUS_CHOICES = (
    ('C1', 'Cancel'),
    ('C2', 'Not Started'),
    ('C3', 'In Progress'),
    ('C4', 'Done')
)

PRIORITY_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
)


class pre_launch_email(models.Model):
    email = models.CharField(max_length=10000)
    #progress_percent = models.FloatField(default=0)
    


def generate_random_url(someparam):
    print(someparam)
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=15))

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

# Create your models here.
class user_project(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    project_name = models.CharField(max_length=5000)
    slug = AutoSlugField(populate_from='project_name', unique_with=['id'], slugify=generate_random_url, unique=True)
    start_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=datetime.now, blank=True)
    #progress_percent = models.FloatField(default=0)


class project_module(models.Model):

    project = models.ForeignKey(user_project, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=5000)
    #progress_percent = models.FloatField(default=0)
    
class project_task(models.Model):

    module = models.ForeignKey(project_module, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=5000, default="Try")
    status = models.CharField(choices=STATUS_CHOICES,max_length=2, default='C2')
    points = models.IntegerField()
    priority_task = models.CharField(choices=PRIORITY_CHOICES,max_length=2, default='N')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

   


