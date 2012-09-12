from django.conf.urls import patterns, url

from apps.students.views import GroupListView

urlpatterns = patterns('',
    url(r'^groups/$', GroupListView.as_view(), name='index-students'),
)
