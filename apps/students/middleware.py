# -*- coding: utf-8 -*-
from time import time

from django.db import connection
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _
from django.template import Template, Context


def replace_insensitive(string, target, replacement):
    """
    https://bitbucket.org/salvator/django-debug-toolbar/src/e455bec46f7b/debug_toolbar/middleware.py
    """
    no_case = string.lower()
    index = no_case.rfind(target.lower())
    if index >= 0:
        return string[:index] + replacement + string[index + len(target):]
    else:
        return string


class RequestStat(object):

    def process_request(self, request):
        self.request_start = time()

    def process_response(self, request, response):
        self.total_time = (time() - self.request_start) * 1000

        if request.META['CONTENT_TYPE'] in ('text/plain', 'text/html'):

            tag = u'</body>'

            response.content = replace_insensitive(
                smart_unicode(response.content),
                tag,
                smart_unicode(self.render_sql_stat_block() + tag))

        return response

    def render_sql_stat_block(self):
        statrows = (
            (_('Total request time'), '%0.3f msec' % self.total_time),
            (_('Sql queries count'), len(connection.queries)),
        )

        t = Template("""
            <table class="stat">
            {% for row in statrows %}
                <tr>
                    <td>{{ row.0 }}</td>
                    <td>{{ row.1 }}</td>
                </tr>
            {% endfor %}
            </table>\n""")

        return t.render(Context({'statrows': statrows}))
