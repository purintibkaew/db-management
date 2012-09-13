from django.conf.urls import patterns, url
from django.contrib.auth.views import logout

from apps.accounts.views import LoginView


urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name='login-accounts'),
    url(r'^logout/$', logout, {'next_page': '/accounts/login/'},
        name='logout-accounts')
)
