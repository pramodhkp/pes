from dajax.core import Dajax
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

from college.models import Project
from django.db.models import Q
from django.core import serializers


# Returns projects containing the search term in title or description.
@dajaxice_register
def get_projects(request, textarea):
	print "test"
	# projects = Project.objects.all()
	projects = Project.objects.filter(Q(name__icontains=str(textarea)) | Q(details__icontains=str(textarea)))
	print projects
	# projects = serializers.serialize('json', projects)
	print [{'name': p.name, 'details': p.details, 'id': p.p_id} for p in projects]
	try:
		return simplejson.dumps({'result' : [{'name': p.name, 'details': p.details, 'id': p.p_id} for p in projects]})
	except Exception as e:
		print e

# Returns members of a particular project based on type (student or teacher).
@dajaxice_register
def get_members(request, id, type):
	print id, type
	project = Project.objects.get(p_id = id)
	print project
	if(type == 'student'):
		students = project.members_s.all()
		print students
		try:
			return simplejson.dumps({'result' : [{'name': s.first_name + ' ' +s.last_name,
													'id' : s.s_id} for s in students]});
		except Exception as e:
			print e
	else:
		teachers = project.members_t.all()
		print teachers
		try:
			return simplejson.dumps({'result' : [{'name': t.first_name + ' ' +t.last_name,
													'id' : t.t_id} for t in teachers]});
		except Exception as e:
			print e
