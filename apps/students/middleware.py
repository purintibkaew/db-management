#-*- coding: utf-8 -*-
import time

from django.template import Template, Context
from django.utils.encoding import smart_unicode


class StatisticMiddleware(object):
    def process_request(self, request):
        self.start_time = time.time()

    def process_response(self, request, response):
        self.total_time = time.time() - self.start_time
        response.content = smart_unicode(response.content) + smart_unicode(self.render())
        return response

    def render(self):
        data = '%s' % self.total_time
        t = Template(""" {{ time }} """)
        return t.render(Context({'time': data}))

