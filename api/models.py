from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

    def __str__(self):
        return self.username


class Project(models.Model):

    title = models.CharField( max_length=50)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    author_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Contributor(models.Model):

    ROLE_CHOICE = (('USER', 'user'), ('ADMIN', 'admin'))

    user_id = models.ManyToManyField(User)
    project_id = models.ManyToManyField(Project)
    permission = models.CharField(max_length=5, choices=ROLE_CHOICE)
    role = models.CharField(max_length=50)
    

class Issue(models.Model):

    PRIORITY_CHOICE = (('L', 'low'), ('M', 'medium'), ('H', 'high'))

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    assignee_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignee')
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):

    description = models.CharField(max_length=100)
    author_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comments_id

