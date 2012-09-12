#-*- coding: utf-8 -*-
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=35)
    date = models.DateField()
    student_ID = models.IntegerField()
    group = models.ForeignKey('Group')

    def __unicode__(self):
        return '%s' % (self.name)


class Group(models.Model):
    name = models.CharField(max_length=35)
    group_senior = models.ForeignKey(Student, related_name='+')

    def __unicode__(self):
        return '%s' % (self.name)
		