from django import forms
from .models import user_project,project_task,project_module, pre_launch_email

class add_project_form(forms.ModelForm):

    deadline = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date', 'class' : 'form-control'} 
        ),
        help_text='Select a date you want to show your product to the world.',
    )   

    class Meta:
        model = user_project
        fields = ['project_name', 'deadline']
        exclude = ['user','slug']
        widgets = {
            'project_name' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 

        }
        

class add_module_form(forms.ModelForm):

    class Meta:
        model = project_module
        fields = ['module_name']
        exclude = ['project']
        widgets = {
            'module_name' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 

        }
        

class add_task_form(forms.ModelForm):

    class Meta:
        model = project_task
        fields = ['task_name', 'status', 'points', 'priority_task']
        exclude = ['module', 'task_name', 'points', 'priority_task']
        widgets = {
            'task_name' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 

            'status' : forms.Select(attrs={
                'class' : 'form-control'
            }), 

            'points' : forms.NumberInput(attrs={
                'class' : 'form-control'
            }), 
        }

class add_task_form_modal(forms.ModelForm):

    class Meta:
        model = project_task
        fields = ['task_name', 'status', 'points', 'priority_task']
        exclude = ['module']
        widgets = {
            'task_name' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 

            'status' : forms.Select(attrs={
                'class' : 'form-control'
            }), 

            'points' : forms.NumberInput(attrs={
                'class' : 'form-control'
            }), 

            'priority_task' : forms.Select(attrs={
                'class' : 'form-control'
            }), 
        }

class pre_launch_email_form(forms.ModelForm):

    class Meta:
        model = pre_launch_email
        fields = ['email']
        widgets = {
            'email' : forms.TextInput(attrs={
                'class' : 'form-control emaillanding',
                'placeholder': 'Email'
            }), 

        }