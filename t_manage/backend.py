from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()


class EmailBackend(ModelBackend):
	def authenticate(self, request, username=None, password=None, **kwargs):
		UserModel = get_user_model()
		try:
			user = UserModel.objects.get(email=username)
		except UserModel.DoesNotExist:
			return None
		else:
			# print(user.check_password(password))
			# if user.check_password(password):
			return user
			# return None
