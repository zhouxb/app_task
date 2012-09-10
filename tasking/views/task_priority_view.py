# -*- coding:utf8 -*-

from annoying.decorators import ajax_request
from tasking.models import Task

@ajax_request
def update(request):
    id_row_data = request.GET.get('id_row_data', '')
    Task.update_priority(id_row_data)
    return {}

