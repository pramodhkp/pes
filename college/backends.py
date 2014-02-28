from django.contrib.auth.models import User, check_password

class EmailAuthBackend(object):
	def authenticate(self, email=None, password=None):
		user = User.objects.get(email=email)

		try:
			if user is not None:
				if user.check_password(password):
					return user				
		except User.DoesNotExist:
			return None


	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None