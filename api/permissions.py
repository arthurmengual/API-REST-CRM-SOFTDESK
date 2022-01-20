from rest_framework.permissions import BasePermission
from . import models


class Project_permission(BasePermission):

    def has_permission(self, request, view):
        pk = view.kwargs['pk']
        project = models.Project.objects.get(pk=pk)
        contributors = models.Contributor.objects.filter(project_id=pk)
        print(contributors)
        if request.user.is_superuser:
            return True
        if view.action in ['update', 'destroy']:
            if request.user == project.author_user_id:
                return True
        elif view.action == 'retrieve':
            if request.user == project.author_user_id:
                return True
            elif contributors.filter(user_id=request.user.id).exists():
                return True
            else:
                return False 
        return True
        
      
class Contributor_permission(BasePermission):

    def has_permission(self, request, view):
        if self.request.user.IsAuthenticated():
            return True
        else:
            return False

    
