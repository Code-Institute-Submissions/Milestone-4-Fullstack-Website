from django.conf.urls import url, include
from about.views import about


urlpatterns = [
    url(r'^about/', about, name="about")
]