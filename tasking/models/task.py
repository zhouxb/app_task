# -*- coding:utf8 -*-

import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from taggit.managers import TaggableManager

class Task(models.Model):
    STATUE = (
        ('N', '新建'),
        ('P', '执行'),
        ('S', '挂起'),
        ('F', '完成'),
        ('C', '关闭')
    )

    user = models.ForeignKey(User);
    description = models.CharField(_('description'), max_length=200)
    statue = models.CharField(_('statue'), max_length=1, choices=STATUE, default='N')
    datetime = models.DateTimeField(_('create time'), default=datetime.datetime.now)
    priority = models.IntegerField(_('priority'), null=True, blank=True)

    tags = TaggableManager()

    class Meta:
        app_label = 'tasking'
        ordering = ['priority',]

    def  __unicode__(self):
        return self.description

    @classmethod
    def update_priority(cls, id_row_data):
        if id_row_data.endswith('|'):
            id_rows = id_row_data[:-1].split('|')
        if id_rows:
            for id_row in id_rows:
                id, row = id_row.split('_')
                cls.objects.filter(id=id).update(priority=row)

