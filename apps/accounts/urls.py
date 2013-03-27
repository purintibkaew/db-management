from django.conf.urls import patterns, url
from django.contrib.auth.views import logout

from accounts.views import LoginView


urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout, {'next_page': '/accounts/login/'},
        name='logout')
)
