from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddProjectForm, EditProjectForm
from projects_show_page.models import Projects
from project_members.models import ProjectMembers
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def create_project_page(request):
	form = AddProjectForm()
	if request.method == "GET":
		return render(request, 'create_project_page.html', {'title': 'Create Project Page', 'forms': form})
	else:
		if Projects.objects.filter(project_name=request.POST['project_name']):
			return render(request, 'create_project_page.html',
						  {'title': 'Create Project Page', 'forms': form, 'error': "Project already exist!"})
		else:
			new_project = Projects(creator_id=request.user, project_name=request.POST['project_name'],
								   project_description=request.POST['description'])
			new_project.save()
			return redirect("projects_show_page:project_show_main_page")


@login_required
def edit_project_page(request, id):
	edit_project = Projects.objects.get(id=id)
	if request.method == "GET":
		form = EditProjectForm(instance=edit_project)
		return render(request, 'edit_project_page.html',
					  {'title': 'Edit Project Page', 'forms': form, 'project_id': edit_project.id})


@login_required
def update_name(request, project_id):
	if request.method == "POST":
		edit_project = Projects.objects.get(id=project_id)
		edit_project.project_name = request.POST['project_name']
		edit_project.save()
		return redirect('add_and_modify:edit_project_page', edit_project.id)


@login_required
def update_description(request, project_id):
	if request.method == "POST":
		edit_project = Projects.objects.get(id=project_id)
		edit_project.project_description = request.POST['project_description']
		edit_project.save()
		return redirect('add_and_modify:edit_project_page', edit_project.id)


@login_required
def add_email_to_project(request, project_id):
	if request.method == "POST":
		edit_project = Projects.objects.get(id=project_id)
		try:
			get_user_throught_email = User.objects.get(email=request.POST['user_email'])
		except:
			return redirect('add_and_modify:edit_project_page', edit_project.id)
		else:
			project_members = ProjectMembers(project_id=edit_project, user_id=get_user_throught_email,
											 role_id=1)
			project_members.save()

			return redirect('projects_show_page:project_show_main_page')


def delete_project(request, project_id):
	if request.method == "POST":
		edit_project = Projects.objects.get(id=project_id)
		edit_project.delete()
		return redirect('projects_show_page:project_show_main_page')
