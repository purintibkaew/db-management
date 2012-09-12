#-*- coding: utf-8 -*-
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=35)
    date = models.DateField()
    student_ID = models.IntegerField()
    group = models.ForeignKey('Group', blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.name)

    @models.permalink
    def get_edit_url(self):
        return ('student_edit-students', [str(self.id)])

    @models.permalink
    def get_del_url(self):
        return ('delete_student-students', [str(self.id)])


class Group(models.Model):
    name = models.CharField(max_length=35)
    group_senior = models.ForeignKey(Student, related_name='+', blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('group_details-students', [str(self.id)])

    @models.permalink
    def get_edit_url(self):
        return ('group_edit-students', [str(self.id)])

    @models.permalink
    def get_del_url(self):
        return ('delete_group-students', [str(self.id)])
