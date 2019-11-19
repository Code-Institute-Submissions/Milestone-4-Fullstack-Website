from django.conf.urls import url, include
from work.views import work, censored_green, city, lady_in_red, protest_target


urlpatterns = [
    url(r'^work/', work, name="work"),
    url(r'^censored_green/', censored_green, name="censored_green"),
    url(r'^city/', city, name="city"),
    url(r'^lady_in_red/', lady_in_red, name="lady_in_red"),
    url(r'^protest_target/', protest_target, name="protest_target")
]