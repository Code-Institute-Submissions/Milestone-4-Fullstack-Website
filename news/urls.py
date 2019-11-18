from django.conf.urls import url, include
from news.views import news 


urlpatterns = [
    url(r'^news/', news, name="news")
]