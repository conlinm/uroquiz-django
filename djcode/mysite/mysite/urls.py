from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead
from uroquiz import views
from django.contrib.auth.views import login, logout
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^search/$', views.search), ('^meta/$', views.display_meta),
    (r'^results/$', views.results), (r'^login/$', views.login), 
    (r'^register/$', views.register),
     (r'^accounts/logout/$', logout), (r'^accounts/login/$', login),
    #(r'^accounts/$', include('registration.urls')),(r'^account/loggedout/$', views.loggedout), (r'^account/loggedin/$', views.loggedin), (r'^account/invalid/$', views.invalid),
    #(r'$', direct_to_template, { 'template': 'index.html'}, 'index'),
    # Examples:
    url(r'^$', views.home, name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
urlpatterns += staticfiles_urlpatterns()