from django.conf.urls import url, include
from news.views import news, looking_for_work


urlpatterns = [
    url(r'^news/', news, name="news"),
    url(r'^news/looking_for_work/', looking_for_work, name="looking_for_work"),
]