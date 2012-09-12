#-*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import FormView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from apps.students.models import Group, Student
from apps.students.forms import GroupForm, StudentForm


class GroupListView(ListView):
    context_object_name = "group_list"
    template_name = "students/group_list.html"

    def get_queryset(self):
    	groups = Group.objects.all()
        return groups


class GroupDetailsView(DetailView):
    model = Group
    context_object_name = "group"
    template_name = 'students/group_details.html'


class EditGroupView(FormView):
    form_class = GroupForm
    template_name = "students/edit_group.html"

    def get_context_data(self, **kwargs):
        kwargs = super(EditGroupView, self).get_context_data(**kwargs)
        kwargs.update({'edit': self.kwargs.get('pk', None)})
        return kwargs

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instanciating the form.
        """
        kwargs = super(EditGroupView, self).get_form_kwargs()

        if self.kwargs.get('pk', None):
            self.group_id = self.kwargs.get('pk', None)
            kwargs.update(
                {'initial': Group.objects.values()[int(self.group_id) - 1]})
            kwargs['initial']['group_senior'] = kwargs['initial']['group_senior_id']

        return kwargs

    def form_valid(self, form):
        group = form.save()
        return HttpResponseRedirect(reverse('group_list-students'))


class EditStudentView(FormView):
    form_class = StudentForm
    template_name = "students/edit_student.html"

    def get_context_data(self, **kwargs):
        kwargs = super(EditStudentView, self).get_context_data(**kwargs)
        kwargs.update({'edit': self.kwargs.get('pk', None)})
        return kwargs

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instanciating the form.
        """
        kwargs = super(EditStudentView, self).get_form_kwargs()

        if self.kwargs.get('pk', None):
            self.student_id = self.kwargs.get('pk', None)
            kwargs.update(
                {'initial': Student.objects.values()[int(self.student_id) - 1]})
            kwargs['initial']['group'] = kwargs['initial']['group_id']

        return kwargs

    def form_valid(self, form):
        student = form.save()
        return redirect(student.group)


class DeleteStudent(DeleteView):
    model = Student
    success_url = '/groups/'
    template_name = 'students/group_details.html'
    template_name_suffix = None


class DeleteGroup(DeleteView):
    model = Group
    success_url = '/groups/'
    template_name = "students/group_list.html"
    template_name_suffix = None