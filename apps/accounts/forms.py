﻿#-*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))
