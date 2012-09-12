from django.conf.urls import patterns, url

from apps.students.views import GroupListView, GroupDetailsView, EditGroupView, EditStudentView, DeleteStudent, DeleteGroup


urlpatterns = patterns('',
    url(r'^groups/$', GroupListView.as_view(), name='group_list-students'),
    url(r'^group/(?P<pk>\d+)/$', GroupDetailsView.as_view(), name='group_details-students'),

    url(r'^group/add/$', EditGroupView.as_view(), name='group_add-students'),
    url(r'^group/(?P<pk>\d+)/edit/$', EditGroupView.as_view(), name='group_edit-students'),

    url(r'^student/(?P<pk>\d+)/edit/$', EditStudentView.as_view(), name='student_edit-students'),
    url(r'^student/add/$', EditStudentView.as_view(), name='student_add-students'),

    url(r'^group/(?P<pk>\d+)/delete$', DeleteGroup.as_view(), name='delete_group-students'),
    url(r'^student/(?P<pk>\d+)/delete$', DeleteStudent.as_view(), name='delete_student-students'),
)
