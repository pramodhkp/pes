from django.conf.urls import patterns, include, url
from college.views import login, logout, home, profile_student, dashboard_student, dashboard_teacher


from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',

	url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    # Examples:
    url(r'^college/home/$', 'college.views.home', name='home'),
    url(r'^college/logout/$', 'college.views.logout', name='logout'),
    url(r'^college/login/$', 'college.views.login', name='login'),
    url(r'^college/student/$', 'college.views.dashboard_student', name='home'),
    url(r'^college/student/(\d+)/$', 'college.views.profile_student', name='profile_student'),
    url(r'^college/teacher/(\d+)/$', 'college.views.profile_teacher', name='profile_teacher'),
    url(r'^college/teacher/evaluate/(\d+)/$', 'college.views.evaluate_project', name='evaluate_project'),
    url(r'^college/projects/(\d+)/$', 'college.views.project_details', name='project_details'),
    url(r'^college/teacher/$', 'college.views.dashboard_teacher', name='home'),
    url(r'^college/editprofile/$', 'college.views.edit_profile', name='edit_profile'),
    url(r'^project/comments/$', include('fluent_comments.urls')),
    (r'^college/messages/', include('postman.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
