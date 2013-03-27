# *- coding: utf-8 -*-
from django import forms

from students.models import Student, Group


class StudentForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Student
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(StudentForm, self).__init__(*args, **kwargs)
        queryset = Group.objects.filter(user=self.user)
        empty_label = 'You have not selected the group'
        if len(queryset) == 0:
            empty_label = 'The list is empty'
        self.fields['group'] = forms.ModelChoiceField(empty_label=empty_label,
                                                      queryset=queryset,
                                                      required=False)

    def save(self, *args, **kwargs):
        student = super(StudentForm, self).save(commit=False)
        id = self.cleaned_data.get('id')
        student.user = self.user
        if id:
            student.id = id
        student = super(StudentForm, self).save()
        return student


class GroupForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Group
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(GroupForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        group = super(GroupForm, self).save(commit=False)
        id = self.cleaned_data.get('id')
        group.user = self.user
        if id:
            group.id = id
        group = super(GroupForm, self).save()
        return group
