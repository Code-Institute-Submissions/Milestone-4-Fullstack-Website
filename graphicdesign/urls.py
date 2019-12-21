"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve

from accounts import urls as urls_accounts
from accounts.views import NeedsForm, index

from products import urls as urls_products
from products.views import all_products

from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout

from django.views import static
from .settings import MEDIA_ROOT

from about import urls as urls_about
from about.views import about

from news import urls as urls_news
from news.views import news, looking_for_work, project_complete, opening

from work import urls as urls_work
from work.views import work, censored_green, city, girl_with_gun_red, protest_target, house, hood_grey,car_lens_flare_blue, smoking_man_brown, storefront_ice

from posts import urls as urls_posts
from posts.views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^products/', all_products, name='products'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url(r'^about/', about , name='about'),
    url(r'^news/', news , name='news'),
    url(r'^news/',include(urls_news)),
    url(r'^work/', work , name='work'),
    url(r'^looking_for_work/', looking_for_work, name="looking_for_work"),
    url(r'^project_complete/', project_complete, name="project_complete"),
    url(r'^opening/', opening, name="opening"),
    url(r'^censored_green/', censored_green, name="censored_green"),
    url(r'^car_lens_flare_blue/', car_lens_flare_blue, name="car_lens_flare_blue"),
    url(r'^smoking_man_brown/', smoking_man_brown, name="smoking_man_brown"),
    url(r'^storefront_ice/', storefront_ice, name="storefront_ice"),
    url(r'^city/', city, name="city"),
    url(r'^house/', house, name="house"),
    url(r'^hood_grey/', hood_grey, name="hood_grey"),
    url(r'^girl_with_gun_red/', girl_with_gun_red, name="girl_with_gun_red"),
    url(r'^protest_target/', protest_target, name="protest_target"),
    url(r'^create_or_edit_post/', create_or_edit_post, name="create_or_edit_post"),
    url(r'^post_detail/', post_detail, name="post_detail"),
    url(r'^get_posts/', get_posts, name="get_posts"),
    url(r'^post$', RedirectView.as_view(url='posts/')),
    url(r'^posts/', include('posts.urls')),
    url(r'^needsform/', NeedsForm, name="NeedsForm"),
]