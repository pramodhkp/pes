from dajax.core import Dajax
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

from college.models import Project
from django.db.models import Q
from django.core import serializers

@dajaxice_register
def get_projects(request, textarea):
	print "test"
	# projects = Project.objects.all()
	projects = Project.objects.filter(Q(name__icontains=str(textarea)) | Q(details__icontains=str(textarea)))
	print projects
	# projects = serializers.serialize('json', projects)
	print [{'name': p.name, 'details': p.details} for p in projects]
	try:
		return simplejson.dumps({'result' : [{'name': p.name, 'details': p.details} for p in projects]})
	except Exception as e:
		print e

