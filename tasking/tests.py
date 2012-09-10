# -*- coding:utf8 -*-

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from monitor.models.state import State
import simplejson

class TaskTest(TestCase):
    fixtures = ['task_testdata.json']

    def setUp(self):
        self.c = Client()

    def test_index(self):
        response = self.c.post(
                    reverse('monitor:state_create'),
                        {
                            'result':'[{"sn":"sn01", "time":"time","normal":[{"url":"http://www.baidu.com", "detail":"30"}], "abnormal":[{"url":"http://www.google.com.hk", "detail":"failure" }]}]'
                        },
                    )

        result = simplejson.loads(response.content)

        result = simplejson.loads(response.content)
        state = State.objects.values('normal_count', 'abnormal_count')[0]
        expect = {'normal_count':1, 'abnormal_count':1}

        assert result['result'] == 'success'
        assert state == expect

