from django.shortcuts import render, redirect
from .models import user_project, project_module, project_task
from .forms import add_project_form, add_module_form, add_task_form, add_task_form_modal
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.template.defaulttags import register
import json
from random import randint
import os
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, time
import pytz
from django.utils import timezone
import random

# Create your views here.

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

classList = [
    'bg-success', 'bg-danger', 'bg-warning', 'bg-info',

]


@register.filter
def random_css(a):
    return random.choice(classList)


@login_required
def scheduler(request):

    projects = user_project.objects.filter(user = request.user)

    projectss = {}
    points = []
    total_task = 0
    task_done = 0
    task_inprogress = 0
    priority_task = [] 
    task_done_per = 0
    task_inprogress_per = 0


    if projects:

        projectss = {}
        points = []
        total_task = 0
        task_done = 0
        task_inprogress = 0
        priority_task = []

        for i in projects:
            # projects[i.name] = i.progress
            tasks = []
            progress_percent = {}
            modules = project_module.objects.filter(project = i)
            for j in modules:
                
                tasks.extend(project_task.objects.filter(module = j))
                priority_task.extend(project_task.objects.filter(module = j, priority_task='Y'))
                sum_done = project_task.objects.filter(module = j, status = 'C4').aggregate(Sum('points'))
                sum_progress = project_task.objects.filter(module = j, status = 'C3').aggregate(Sum('points'))
                sum_total = project_task.objects.filter(module = j).aggregate(Sum('points'))
                # print(sum_done,sum_progress, sum_total)
                
                if sum_done['points__sum']==None:
                    sum_done['points__sum'] = 0
                
                if sum_progress['points__sum']==None:
                    sum_progress['points__sum'] = 0

                if sum_total['points__sum'] !=0 and sum_total['points__sum'] !=None:
                    progress_percent[j.id] = ((sum_done['points__sum'] + sum_progress['points__sum']/2)/sum_total['points__sum'])*100
                # progress_done_points[i.id] = sum_done['points__sum'] + int(sum_progress['points__sum']/2)
                else:
                    progress_percent[j.id] = 0
            # for i in modules:
            #     # print(i.module_name)
            #     for task in tasks:
            #         print(i.module_name, task.module.module_name)
            # print(tasks)

            # print(module_points_sum)

            total_progress_percent = sum(progress_percent.values())
            total_modules_percent = len(progress_percent)*100

            if total_modules_percent !=0:
                final_progress = (total_progress_percent/total_modules_percent)*100
                projectss[i.project_name] = final_progress
            else:
                final_progress = 0
                projectss[i.project_name] = 0
            # ####Quote
            # # print(random_quote())
            # quote = random_quote()

            # # print(quote)
            # quotee = quote['text']
            # quote_a = quote['author']

            # today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            # today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
            # # Invoice.objects.get(user=user, date__range=(today_min, today_max))

            today = timezone.now()
            tomorrow = today + timedelta(1)
            today_start = datetime.combine(today, time())
            today_end = datetime.combine(tomorrow, time())


            points_today = 0
            
            for k in tasks:
                total_task+=1
                # print('All: ',i.task_name, i.updated_at, i.status)
                if k.status == 'C4':
                    task_done+=1
                
                if k.status == 'C3':
                    task_inprogress+=1

                if (k.status == 'C4' or k.status == 'C3') and k.updated_at.replace(tzinfo=None)>=today_start and k.updated_at.replace(tzinfo=None)<=today_end:
                    # print('Chosen Ones: ',i.task_name, i.updated_at)
                    if k.status == 'C4':
                        points_today += k.points
                        # task_done+=1
                    else:
                        points_today += int(k.points/2)
                        # task_inprogress+=1

            points.append(points_today)
            
    if total_task!=0:
        task_done_per = (task_done/total_task) * 100
        task_inprogress_per = (task_inprogress/total_task) * 100


    return render(request, "scheduler/index.html", {'projectss':projectss, 'points':sum(points), 'total_proj' : len(projectss), 'total_task': total_task, 'task_done': task_done, 'task_inprogress': task_inprogress, 'task_inprogress_per': task_inprogress_per, 'task_done_per': task_done_per, 'priority_task':priority_task})


def try_progress(request):

    return render(request, "scheduler/try_progress_bar.html")

def random_quote():

    dirpath = os.path.dirname(os.path.abspath(__file__))
    qp = os.path.join(dirpath, 'quotes.json')

    with open(qp) as quotes:
        data = json.load(quotes)
        # print(data)
        random_index = randint(0, len(data)-1)
        return data[random_index]

@login_required
def projects(request, slug):

    projects = user_project.objects.filter(user = request.user, slug = slug)
    # projects = user_project.objects.filter(slug = slug)

    # print('Finding errorrrr:', projects)

    if projects:

        for i in projects:
            project_id = i.id
            project_name = i.project_name
            modules = project_module.objects.filter(project = i)
            start_date = i.start_date

        # modules = project_module.objects.filter(project = projects)

        # print(modules)

        tasks = []
        progress_percent = {}

        for i in modules:
            
            tasks.extend(project_task.objects.filter(module = i))
            sum_done = project_task.objects.filter(module = i, status = 'C4').aggregate(Sum('points'))
            sum_progress = project_task.objects.filter(module = i, status = 'C3').aggregate(Sum('points'))
            sum_total = project_task.objects.filter(module = i).aggregate(Sum('points'))
            # print(sum_done,sum_progress, sum_total)
            
            if sum_done['points__sum']==None:
                sum_done['points__sum'] = 0
            
            if sum_progress['points__sum']==None:
                sum_progress['points__sum'] = 0

            if sum_total['points__sum'] !=0 and sum_total['points__sum'] !=None:
                progress_percent[i.id] = ((sum_done['points__sum'] + sum_progress['points__sum']/2)/sum_total['points__sum'])*100
            # progress_done_points[i.id] = sum_done['points__sum'] + int(sum_progress['points__sum']/2)
            else:
                progress_percent[i.id] = 0
        # for i in modules:
        #     # print(i.module_name)
        #     for task in tasks:
        #         print(i.module_name, task.module.module_name)
        # print(tasks)

        # print(module_points_sum)

        total_progress_percent = sum(progress_percent.values())
        total_modules_percent = len(progress_percent)*100

        if total_modules_percent !=0:
            final_progress = (total_progress_percent/total_modules_percent)*100
        else:
            final_progress = 0

        ####Quote
        # print(random_quote())
        quote = random_quote()

        # print(quote)
        quotee = quote['text']
        quote_a = quote['author']

        # today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        # today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        # # Invoice.objects.get(user=user, date__range=(today_min, today_max))

        today = timezone.now()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())


        points_today = 0
        
        for i in tasks:
            # print('All: ',i.task_name, i.updated_at, i.status)

            if (i.status == 'C4' or i.status == 'C3') and i.updated_at.replace(tzinfo=None)>=today_start and i.updated_at.replace(tzinfo=None)<=today_end:
                # print('Chosen Ones: ',i.task_name, i.updated_at)
                if i.status == 'C4':
                    points_today += i.points
                else:
                    points_today += int(i.points/2)

        
        return render(request, "scheduler/project.html", {'quote':quotee, 'quote_a': quote_a, 'final_progress':final_progress,'progress_percent': progress_percent, 'modules': modules, 'tasks':tasks,'project_name':project_name,'project_id':project_id, 'add_module_form':add_module_form, 'add_task_form': add_task_form, 'add_task_form_modal': add_task_form_modal, 'points_today':points_today, 'slug': slug, 'start_date': start_date})
    
    else:

        projects = user_project.objects.filter(slug = slug)

        for i in projects:
            project_id = i.id
            project_name = i.project_name
            project_dev = i.user
            modules = project_module.objects.filter(project = i)
        # modules = project_module.objects.filter(project = projects)

        # print(modules)

        tasks = []
        progress_percent = {}

        for i in modules:
            
            tasks.extend(project_task.objects.filter(module = i))
            sum_done = project_task.objects.filter(module = i, status = 'C4').aggregate(Sum('points'))
            sum_progress = project_task.objects.filter(module = i, status = 'C3').aggregate(Sum('points'))
            sum_total = project_task.objects.filter(module = i).aggregate(Sum('points'))
            # print(sum_done,sum_progress, sum_total)
            
            if sum_done['points__sum']==None:
                sum_done['points__sum'] = 0
            
            if sum_progress['points__sum']==None:
                sum_progress['points__sum'] = 0

            if sum_total['points__sum'] !=0:
                progress_percent[i.id] = ((sum_done['points__sum'] + sum_progress['points__sum']/2)/sum_total['points__sum'])*100
            # progress_done_points[i.id] = sum_done['points__sum'] + int(sum_progress['points__sum']/2)
            else:
                progress_percent[i.id] = 0
        # for i in modules:
        #     # print(i.module_name)
        #     for task in tasks:
        #         print(i.module_name, task.module.module_name)
        # print(tasks)

        # print(module_points_sum)

        total_progress_percent = sum(progress_percent.values())
        total_modules_percent = len(progress_percent)*100

        if total_modules_percent !=0:
            final_progress = (total_progress_percent/total_modules_percent)*100
        else:
            final_progress = 0

        ####Quote
        # print(random_quote())
        quote = random_quote()

        # print(quote)
        quotee = quote['text']
        quote_a = quote['author']

        # today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        # today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        # # Invoice.objects.get(user=user, date__range=(today_min, today_max))

        today = timezone.now()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())


        points_today = 0
        
        for i in tasks:
            # print('All: ',i.task_name, i.updated_at, i.status)

            if (i.status == 'C4' or i.status == 'C3') and i.updated_at.replace(tzinfo=None)>=today_start and i.updated_at.replace(tzinfo=None)<=today_end:
                # print('Chosen Ones: ',i.task_name, i.updated_at)
                if i.status == 'C4':
                    points_today += i.points
                else:
                    points_today += int(i.points/2)


        return render(request, "scheduler/project_shared.html", {'project_dev' : project_dev, 'quote':quotee, 'quote_a': quote_a, 'final_progress':final_progress,'progress_percent': progress_percent, 'modules': modules, 'tasks':tasks,'project_name':project_name,'project_id':project_id, 'add_module_form':add_module_form, 'add_task_form': add_task_form, 'add_task_form_modal': add_task_form_modal, 'points_today':points_today})
    

def add_project(request):
    projectform = add_project_form(request.POST)

    if projectform.is_valid():
        print('Project added success')
        projectformsave = projectform.save(commit=False)
        projectformsave.user = request.user
        projectformsave.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add_module(request,pk):
    moduleform = add_module_form(request.POST)

    project = user_project.objects.filter(id = pk)

    for i in project:
        proj = i

    if moduleform.is_valid():
        print('Module added success')
        moduleformsave = moduleform.save(commit=False)
        moduleformsave.project = proj
        moduleformsave.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_module(request, pk):
    m_obj = project_module.objects.get(id=pk)
    # print(m_obj.project.user)
    if m_obj.project.user == request.user:
        m_obj.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add_task(request,pk):
    taskform = add_task_form_modal(request.POST)

    module = project_module.objects.filter(id = pk)

    for i in module:
        mod = i

    if taskform.is_valid():
        print('Task added success')
        taskformsave = taskform.save(commit=False)
        taskformsave.module = mod
        taskformsave.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_task(request, pk):
    t_obj = project_task.objects.get(id=pk)

    if t_obj.module.project.user == request.user:
        t_obj.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def edit_task(request, pk):
    s_obj = project_task.objects.get(id = pk)
    print('here in edit task')

    print(pk)


    choice = {'Cancel':'C1','Not Started':'C2','In Progress':'C3','Done':'C4'}

    if request.method == "POST":
        form = add_task_form(request.POST, instance=s_obj) #request.FILES
        print(request.POST)
        if form.is_valid():
            print('success Edit Task')
            # formsave = form.save(commit=False)
            # formsave.image = request.FILES['image']
            taskformsave = form.save(commit=False)
            taskformsave.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print('error')
    else:
        print('Errorrrr!!!')
        form = add_task_form(instance=s_obj)

    context = {
        'form' : form,
        'form_id':pk
    }
 
    # return render(request,"admindash/edit_items.html",context)
    return render(request, "scheduler/edit_task.html",context)
