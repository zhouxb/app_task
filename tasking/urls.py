from django.conf.urls.defaults import *

urlpatterns = patterns('tasking.views.task_view',
    url(r'^task/index$', 'index', name='tasking_task_index'),
    url(r'^task/create$', 'create', name='tasking_task_create'),
    url(r'^task/(?P<id>\d+)/update$', 'update', name='tasking_task_update'),
    url(r'^task/(?P<id>\d+)/delete$', 'delete', name='tasking_task_delete'),
)
urlpatterns += patterns('tasking.views.task_priority_view',
    url(r'^task/priority/update$', 'update', name='tasking_task_priority_update'),
)
