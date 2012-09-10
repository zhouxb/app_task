# -*- coding:utf8 -*-

from django import forms
from tasking.models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ('user', 'datetime', 'priority', 'statue')

