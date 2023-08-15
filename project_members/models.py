from django.db import models
from django.contrib.auth import get_user_model
from projects_show_page.models import Projects

User = get_user_model()


class RoleType(models.Model):
	id = models.IntegerField(primary_key=True, unique=True, default=id)
	role_name = models.CharField(null=True, max_length=10)


class ProjectMembers(models.Model):
	project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	role = models.ForeignKey(RoleType, on_delete=models.CASCADE)
