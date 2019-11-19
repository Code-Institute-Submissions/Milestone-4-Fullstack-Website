from django.conf.urls import url, include
from news.views import news, looking_for_work, project_complete, opening


urlpatterns = [
    url(r'^news/', news, name="news"),
    url(r'^looking_for_work/', looking_for_work, name="looking_for_work"),
    url(r'^project_complete/', project_complete, name="project_complete"),
    url(r'^opening/', opening, name="opening"),
]