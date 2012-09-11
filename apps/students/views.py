#-*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect

from apps.students.models import Group


class GroupListView(ListView):
    context_object_name = "group_list"
    template_name = "students/group_list.html"

    def get_queryset(self):
    	groups = Group.objects.all()
        return groups


