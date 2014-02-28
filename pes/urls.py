from django.conf.urls import patterns, include, url
from college.views import login, logout, home


from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',

	url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
	
    # Examples:
    url(r'^college/$', 'college.views.home', name='home'),
    url(r'^college/logout/$', 'college.views.logout', name='logout'),
    url(r'^college/login/$', 'college.views.login', name='login'),
    url(r'^college/main/$', 'college.views.dashboard', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) 
