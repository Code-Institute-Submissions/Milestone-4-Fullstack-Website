from django.conf.urls import url, include
from home.views import about, news 


urlpatterns = [
    url(r'^about/', about, name="about"),
    url(r'^news/', news, name="news")
]