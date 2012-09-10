# -*- coding:utf8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from annoying.decorators import render_to, ajax_request
from tasking.models import Task
from tasking.forms.task_form import TaskForm


@render_to('tasking/task/index.haml')
def index(request):
    user = request.user
    tasks = user.task_set.all()
    return {'tasks':tasks}

@render_to('tasking/task/new.haml')
def create(request):

    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.priority = request.user.task_set.count() + 1
            task.save()
            return HttpResponseRedirect(reverse('tasking_task_index'))
    else:
        form = TaskForm()

    return {'form':form}

@ajax_request
def update(request, id):
    return {'result':'success'}

@ajax_request
def delete(request, id):
    response = {}
    response['result'] = 'success'
    try:
        Task.objects.get(id=id).delete()
    except:
        response['result'] = 'failure'
    return response

