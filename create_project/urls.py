from .views import create_project_page, edit_project_page, update_name, update_description, add_email_to_project,delete_project
from django.urls import path

app_name = 'add_and_modify'

urlpatterns = [
	path('', create_project_page, name='create_project_page'),
	path('edit_project_page/<int:id>/', edit_project_page, name='edit_project_page'),
	path('update_name/<int:project_id>/', update_name, name='update_name'),
	path('update_description/<int:project_id>/', update_description, name='update_description'),
	path('add_email_to_project/<int:project_id>/', add_email_to_project, name='add_email_to_project'),
	path('delete_project/<int:project_id>/', delete_project, name='delete_project'),

]
