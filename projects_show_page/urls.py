from .views import project_show_main_page, logout_user
from django.urls import path

app_name = 'projects_show_page'

urlpatterns = [
	path('', project_show_main_page, name='project_show_main_page'),
	path('logout/', logout_user, name='logout_user'),

]
