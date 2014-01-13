from django.conf.urls import patterns, include, url

from CheckoutSystem import views

from django.contrib import admin
from CheckoutSystem.views import password_reset_placeholder

handler404 = views.custom_404_view

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^welcome/$', views.index),
                       url(r'^progress/$', views.progress),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^accounts/logout/$', views.logout_view),
                       url(r'^accounts/password/reset/$', password_reset_placeholder),
                       url(r'^checkout/', include('checkout.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )


