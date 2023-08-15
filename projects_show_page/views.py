from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Projects
from project_members.models import ProjectMembers


@login_required
def project_show_main_page(request):
	try:
		list_of_my_projects = []
		my_projects = Projects.objects.filter(creator_id=request.user.id)

		for i in my_projects:
			list_of_my_projects.append({
				'main_user': i.creator_id.username,
				'project_name': i.project_name,
				'project_description': i.project_description,
				'project_id': i.id
			})

		list_of_all_projects = []
		all_projects = Projects.objects.all()

		for i in all_projects:
			list_of_all_projects.append({
				'main_user': i.creator_id.username,
				'project_name': i.project_name,
				'project_description': i.project_description
			})

		list_of_shared_projects = []
		project_members = ProjectMembers.objects.filter(user_id=request.user.id)

		for i in project_members:
			projects = Projects.objects.filter(id=i.project_id.id)
			for j in projects:
				list_of_shared_projects.append({
					'added_user': i.user_id.username,
					'main_user': j.creator_id.username,
					'project_name': j.project_name,
					'project_description': j.project_description,
					'project_id': j.id
				})

		return render(request, 'project_show_page.html',
					  {'title': 'project_show_page', 'shared_with_me': list_of_shared_projects,
					   'all_projects': list_of_all_projects, 'created_by_me': list_of_my_projects})
	except:
		my_projects = Projects.objects.filter(creator_id_id=request.user.id)
		return render(request, 'project_show_page.html', {'title': 'project_show_page', 'shared_with_me': '',
														  'all_projects': '', 'created_by_me': ''})


@login_required
def logout_user(request):
	if request.method == "POST":
		logout(request)
		return redirect('t_manage:main_page')
