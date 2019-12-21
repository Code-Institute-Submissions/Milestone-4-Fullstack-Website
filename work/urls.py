from django.conf.urls import url, include
from work.views import work, censored_green, city, girl_with_gun_red, protest_target, house, hood_grey, car_lens_flare_blue, smoking_man_brown, storefront_ice

urlpatterns = [
    url(r'^work/', work, name="work"),
    url(r'^censored_green/', censored_green, name="censored_green"),
    url(r'^city/', city, name="city"),
    url(r'^house/', house, name="house"),
    url(r'^hood_grey/', hood_grey, name="hood_grey"),
    url(r'^girl_with_gun_red/', girl_with_gun_red, name="girl_with_gun_red"),
    url(r'^protest_target/', protest_target, name="protest_target"),
    url(r'^car_lens_flare_blue/', car_lens_flare_blue, name="car_lens_flare_blue"),
    url(r'^smoking_man_brown/', smoking_man_brown, name="smoking_man_brown"),
    url(r'^storefront_ice/', storefront_ice, name="storefront_ice"),
]