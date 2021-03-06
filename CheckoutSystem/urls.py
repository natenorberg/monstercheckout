from django.conf.urls import patterns, include, url

from CheckoutSystem import views

from django.contrib import admin

handler400 = views.custom_400_view
handler403 = views.custom_403_view
handler404 = views.custom_404_view
handler500 = views.custom_500_view
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^welcome/$', views.index),
                       url(r'^progress/$', views.progress),
                       url(r'^account/', include('django.contrib.auth.urls')),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^accounts/logout/$', views.logout_view),
                       url(r'^accounts/profile/$', views.index, name='index'),
                       url(r'^checkout/', include('checkout.urls')),
                       url(r'^admin/', include(admin.site.urls))
                       )


