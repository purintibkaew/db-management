#-*- coding: utf-8 -*-
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from apps.accounts.forms import LoginForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = "registration/login.html"

    def form_valid(self, form):
        kwargs = self.get_form_kwargs()
        username = kwargs['data']['username']
        password = kwargs['data']['password']
        status = kwargs['data']['status']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            if status == 'new':
                user = User.objects.create_user(username=username,
                                                password=password)
                status = 'existing'
            else:
                err_log = _('User not found')
                return self.render_to_response(
                    self.get_context_data(form=form, err_log=err_log))

        if status == 'new':
            err_log = _('This login is already in use')
            return self.render_to_response(
                self.get_context_data(form=form, err_log=err_log))

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect(reverse('group_list-students'))
            else:
                err_log = _('This account is disabled')
                return self.render_to_response(
                    self.get_context_data(form=form, err_log=err_log))

        else:
            err_log = _('Invalid login or password')
            return self.render_to_response(
                self.get_context_data(form=form, err_log=err_log))
