from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Projects(models.Model):
	project_name = models.CharField(max_length=50, unique=True)
	project_description = models.TextField(max_length=200)
	creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
