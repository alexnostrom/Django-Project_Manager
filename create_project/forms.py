from django import forms
from django.forms.models import ModelForm
from projects_show_page.models import Projects


class AddProjectForm(forms.Form):
	project_name = forms.CharField(label="Project Name:",
								   widget=forms.TextInput(
									   attrs={"class": "add_project", "placeholder": "Project name"}),
								   max_length=50)
	description = forms.CharField(label="Description:",
								  widget=forms.Textarea(
									  attrs={"rows": "10", "class": "descrip_project", "placeholder": "Description"}),
								  max_length=300)


class EditProjectForm(forms.Form, ModelForm):
	project_name = forms.CharField(label="Project Name:",
								   widget=forms.TextInput(
									   attrs={"class": "add_project", "placeholder": "Project name"}),
								   max_length=50)
	project_description = forms.CharField(label="Description:",
								  widget=forms.Textarea(
									  attrs={"rows": "10", "class": "descrip_project", "placeholder": "Description"}),
								  max_length=300)
	user_email = forms.CharField(label="User Email:",
								 widget=forms.TextInput(
									 attrs={"class": "add_project", "placeholder": "User Email to add"}), max_length=50)

	class Meta:
		model = Projects
		fields = '__all__'
		exclude = ('created_at',)
