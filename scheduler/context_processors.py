from .models import user_project
from .forms import add_project_form


def projects(request):

    if request.user.is_authenticated:

        project = user_project.objects.filter(user = request.user).order_by('start_date').reverse()

        return {
            'projects': project,
            'add_project_form':add_project_form
        }

    return {
        'projects': None,
        'add_project_form':None
    }    

