from django.conf.urls import patterns, include, url
from college.views import login, logout, home, profile_student, dashboard_student, dashboard_teacher


from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',

	url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    # Examples:
    url(r'^$', 'college.views.main', name='main'),
    url(r'^college/$', 'college.views.main', name='main'),
    url(r'^college/faq/$', 'college.views.faq', name='faq'),
    url(r'^college/about/$', 'college.views.about', name='about'),
    url(r'^college/manual/$', 'college.views.manual', name='manual'),
    url(r'^college/contact/$', 'college.views.contact', name='main'),
    url(r'^college/main/$', 'college.views.main', name='main'),
    url(r'^college/home/$', 'college.views.home', name='home'),
    url(r'^college/logout/$', 'college.views.logout', name='logout'),
    url(r'^college/login/$', 'college.views.login', name='login'),
    url(r'^college/student/$', 'college.views.dashboard_student', name='home'),
    url(r'^college/student/upload/$', 'college.views.file_upload', name='file_upload'),
    url(r'^college/student/upload_success/$', 'college.views.upload_sucess', name='upload_sucess'),
    url(r'^college/reportlist/$', 'college.views.report_list', name='report_list'),
    url(r'^college/report/(\d+)/$', 'college.views.project_report', name='project_report'),
    url(r'^college/student/projectlist/$', 'college.views.project_list_student', name='projectlist'),
    url(r'^college/teacher/projectlist/$', 'college.views.project_list_teacher', name='projectlist'),
    url(r'^college/student/(\d+)/$', 'college.views.profile_student', name='profile_student'),
    url(r'^college/teacher/(\d+)/$', 'college.views.profile_teacher', name='profile_teacher'),
    url(r'^college/teacher/download/(\d+)/$', 'college.views.file_download', name='download'),
    url(r'^college/teacher/evaluate/(\d+)/$', 'college.views.evaluate_project', name='evaluate_project'),
    url(r'^college/projects/(\d+)/$', 'college.views.project_details', name='project_details'),
    url(r'^college/teacher/$', 'college.views.dashboard_teacher', name='home'),
    url(r'^college/editprofile/$', 'college.views.edit_profile', name='edit_profile'),
    (r'^college/messages/', include('postman.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
