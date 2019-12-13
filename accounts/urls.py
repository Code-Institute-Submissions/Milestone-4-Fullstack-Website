from django.conf.urls import url, include
from . import urls_reset
from .views import index, register, profile, logout, login, NeedsForm

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
    url(r'^profile/id', profile, name='profile'),
    url(r'^needsform/$', NeedsForm, name='NeedsForm'),
    url(r'^(?P<pk>\d+)/edit/$', NeedsForm, name='editNeedsForm')
]