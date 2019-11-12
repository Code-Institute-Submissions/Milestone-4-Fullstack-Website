from django.conf.urls import url, include
from home.views import about, news, work 


urlpatterns = [
    url(r'^about/', about, name="about"),
    url(r'^news/', news, name="news"),
    url(r'^work/', work, name="work")
]