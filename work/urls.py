from django.conf.urls import url, include
from work.views import work 


urlpatterns = [
    url(r'^work/', work, name="work")
]