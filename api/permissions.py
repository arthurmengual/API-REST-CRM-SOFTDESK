from lib2to3.pytree import Base
from rest_framework.permissions import BasePermission
from . import models


class Project_permission(BasePermission):

    def has_object_permission(self, request, view, obj):
        contributors = models.Contributor.objects.filter(project_id=obj.id)
        if request.user.is_superuser:
            return True
        elif view.action in ['update', 'destroy']:
            if request.user == obj.author_user_id:
                return True
        elif view.action == 'retrieve':
            if request.user == obj.author_user_id:
                return True
            for contributor in contributors:
                contribs = contributor.user_id.all()
                for contrib in contribs:
                    if request.user == contrib:
                        return True
        elif view.action == 'create':
            return True
        else:
            return False


      
class Contributor_permission(BasePermission):

    def has_permission(self, request, view):
        project_id = view.kwargs['project_pk']
        project = models.Project.objects.get(author_user_id=project_id)
        project_author = project.author_user_id
        if request.user.is_superuser:
            return True
        elif request.user == project_author:
            return True
        else:
            return False

class Issue_permission(BasePermission):

    def has_permission(self, request, view):
        project_id = view.kwargs['project_pk']
        project = models.Project.objects.get(id=project_id)
        project_author = project.author_user_id
        contributors = models.Contributor.objects.filter(project_id=project_id)
        if request.user.is_superuser:
            return True
        elif view.action in ['update', 'destroy']:
            issue = models.Issue.objects.get(id=view.kwargs['pk'])
            if request.user == issue.author_user_id:
                return True
            else:
                return False
        elif view.action in ['create', 'list']:
            if request.user == project_author:
                return True
            for contributor in contributors:
                contribs = contributor.user_id.all()
                for contrib in contribs:
                    if request.user == contrib:
                        return True
            else:
                return False
        else:
            return False


class Comment_permission(BasePermission):

    def has_permission(self, request, view):
        project_id = view.kwargs['project_pk']
        project = models.Project.objects.get(id=project_id)
        project_author = project.author_user_id
        contributors = models.Contributor.objects.filter(project_id=project_id)
        if request.user.is_superuser:
            return True
        elif view.action in ['update', 'destroy']:
            comment = models.Comment.objects.get(id=view.kwargs['pk'])
            if request.user == comment.author_user_id:
                return True
            else:
                return False
        elif view.action in ['create', 'list', 'retrieve']:
            if request.user == project_author:
                return True
            for contributor in contributors:
                contribs = contributor.user_id.all()
                for contrib in contribs:
                    if request.user == contrib:
                        return True
            else:
                return False
        else:
            return False
