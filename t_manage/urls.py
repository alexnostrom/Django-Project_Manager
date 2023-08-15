from .views import main_page, signupuser, loginuser
from django.urls import path

app_name = 't_manage'

urlpatterns = [
	path('', main_page, name='main_page'),
	path('loginuser/', loginuser, name='loginuser'),
	path('signupuser/', signupuser, name='signupuser'),
]
