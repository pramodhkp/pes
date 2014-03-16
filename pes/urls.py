from django.conf.urls import patterns, include, url
from college.views import login, logout, home, profile_student, dashboard_student, dashboard_teacher


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
    url(r'^college/student/$', 'college.views.dashboard_student', name='home'),
    url(r'^college/student/(\d+)/$', 'college.views.profile_student', name='profile_student'),
    url(r'^college/teacher/$', 'college.views.dashboard_teacher', name='home'),
    (r'^college/messages/', include('postman.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
