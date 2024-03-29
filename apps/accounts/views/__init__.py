#-*- coding: utf-8 -*-
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from accounts.forms import LoginForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = "registration/login.html"

    def form_valid(self, form):
        kwargs = self.get_form_kwargs()

        username = kwargs['data']['username']
        password = kwargs['data']['password']

        user = authenticate(
            username=username, email=username, password=password)
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
