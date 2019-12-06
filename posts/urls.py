from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    url(r'^get_posts/$', get_posts, name='get_posts'),
    url(r'^post_detail/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post')
]