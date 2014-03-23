from django.contrib import admin
from college.models import Student, Teacher, Project, Evaluation


class StudentAdmin(admin.ModelAdmin):
	list_display = ('s_id', 'first_name', 'last_name', 'email')

class TeacherAdmin(admin.ModelAdmin):
	list_display = ('t_id', 'first_name', 'last_name', 'email')

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name',)

class EvaluationAdmin(admin.ModelAdmin):
	list_display = ('project', 'score', 'progress', 'timestamp')

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Evaluation, EvaluationAdmin)
# Register your models here.
