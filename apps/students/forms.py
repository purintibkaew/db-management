#-*- coding: utf-8 -*-
from django import forms

from apps.students.models import Student, Group


class StudentForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Student

    def __init__(self, *args, **kwargs):
        self.student_id = None
        super(StudentForm, self).__init__(*args, **kwargs)

        if 'data' in kwargs:
            if 'id' in kwargs['data']:
                self.student_id = kwargs['data']['id']

    def save(self, *args, **kwargs):
        student = super(StudentForm, self).save(commit=False)
        if self.student_id:
            student.id = self.student_id
        student = super(StudentForm, self).save()
        return student


class GroupForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Group

    def __init__(self, *args, **kwargs):
        self.car_id = None
        super(GroupForm, self).__init__(*args, **kwargs)

        if 'data' in kwargs:
            if 'id' in kwargs['data']:
                self.group_id = kwargs['data']['id']

    def save(self, *args, **kwargs):
        group = super(GroupForm, self).save(commit=False)
        if self.group_id:
            group.id = self.group_id
        group = super(GroupForm, self).save()
        return group
