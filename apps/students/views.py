#-*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import FormView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from apps.students.models import Group, Student
from apps.students.forms import GroupForm, StudentForm
from apps.accounts.views.mixinx import LoginRequiredMixin


class GroupListView(LoginRequiredMixin, ListView):
    context_object_name = "group_list"
    template_name = "students/group_list.html"

    def get_queryset(self):
    	groups = Group.objects.filter(user=self.request.user)
        return groups


class GroupDetailsView(LoginRequiredMixin, DetailView):
    model = Group
    context_object_name = "group"
    template_name = 'students/group_details.html'


class EditGroupView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = "students/edit_group.html"

    def get_object(self):
        if self.kwargs.get('pk', None):
            return super(EditGroupView, self).get_object()
        return None

    def get_queryset(self):
        return super(EditGroupView, self).get_queryset().filter(
            user=self.request.user)

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instanciating the form.
        """
        kwargs = super(EditGroupView, self).get_form_kwargs()

        if self.kwargs.get('pk', None):
            self.group_id = int(self.kwargs.get('pk'))
            kwargs.update(
                {'initial': Group.objects.filter(id=self.group_id).values()[0]})
            kwargs['initial']['group_senior'] = kwargs['initial']['group_senior_id']

        return kwargs

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('group_list-students'))


class EditStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "students/edit_student.html"

    def get_object(self):
        if self.kwargs.get('pk', None):
            return super(EditStudentView, self).get_object()
        return None

    def get_queryset(self):
        return super(EditStudentView, self).get_queryset().filter(
            user=self.request.user)

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instanciating the form.
        """
        kwargs = super(EditStudentView, self).get_form_kwargs()

        if self.kwargs.get('pk', None):
            self.student_id = self.kwargs.get('pk', None)
            kwargs.update(
                {'initial': Student.objects.filter(id=self.student_id).values()[0]})
            kwargs['initial']['group'] = kwargs['initial']['group_id']

        return kwargs

    def form_valid(self, form):
        student = form.save()
        return redirect(student.group)


class DeleteStudent(LoginRequiredMixin, DeleteView):
    model = Student

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.object.group)


class DeleteGroup(LoginRequiredMixin, DeleteView):
    model = Group

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(reverse('group_list-students'))
