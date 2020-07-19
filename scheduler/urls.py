from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.landing, name = 'landing'),
    path('app/', views.scheduler, name = 'scheduler'),
    path('paymentsuccess/', views.paymentsuccess, name = 'paymentsuccess'),
    path('paymentsettings/', views.paymentsettings, name = 'paymentsettings'),
    path('app/project/<slug>', views.projects, name = 'project'),
    path('add-project/', views.add_project, name='add_project'),
    path('add-module/<pk>', views.add_module, name='add_module'),
    path('delete-module/<pk>', views.delete_module, name='delete_module'),
    path('add-task/<pk>', views.add_task, name='add_task'),
    path('delete-task/<pk>', views.delete_task, name='delete_task'),
    path('app/project/edit-task/<pk>', views.edit_task, name='edit_task'),
    path('edit-task/<pk>', views.edit_task, name='edit_task'),
    path('app/project/edit-task/', views.edit_task, name='edit_task'),
    path('try-progress/', views.try_progress, name='try_progress'),
    path('add-email-launch/', views.add_email_launch, name='add_email_launch'),

    path('demo/', views.scheduler_demo, name = 'scheduler_demo'),
    path('demoapp/project/<slug>', views.projects_demo, name = 'project_demo'),
]

