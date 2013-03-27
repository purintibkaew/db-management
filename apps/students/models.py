#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.contenttypes import generic


class Student(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=35)
    date = models.DateField()
    student_ID = models.IntegerField()
    group = models.ForeignKey('Group')

    def __unicode__(self):
        return '%s' % self.name

    @models.permalink
    def get_edit_url(self):
        return 'student_edit-students', [str(self.id)]

    @models.permalink
    def get_del_url(self):
        return 'delete_student-students', [str(self.id)]


class Group(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=35)
    group_senior = models.ForeignKey(Student, related_name='+',
                                     blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.name

    @models.permalink
    def get_absolute_url(self):
        return 'group_details-students', [str(self.id)]

    @models.permalink
    def get_edit_url(self):
        return 'group_edit-students', [str(self.id)]

    @models.permalink
    def get_del_url(self):
        return 'delete_group-students', [str(self.id)]


class ModelChangeLog(models.Model):
    ACTION_CHOICES = (
        ('c', 'created'),
        ('m', 'modified'),
        ('d', 'deleted')
    )

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    action = models.CharField(max_length=1, choices=ACTION_CHOICES)

    def __unicode__(self):
        return 'Content type: %s' % self.content_type


@receiver(post_save, sender=Student)
@receiver(post_save, sender=Group)
def post_save_handler(sender, created, instance, **kwargs):
    if created:
        action = 'c'
    else:
        action = 'm'

    ModelChangeLog.objects.create(
        content_object=instance, object_id=instance.id, action=action)


@receiver(post_delete, sender=Student)
@receiver(post_delete, sender=Group)
def post_delete_handler(sender, instance, **kwargs):
    ModelChangeLog.objects.create(
        content_object=instance, object_id=instance.id, action='d')
