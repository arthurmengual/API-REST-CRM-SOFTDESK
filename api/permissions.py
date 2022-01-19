from rest_framework.permissions import BasePermission
from . import models


class Is_user_author(BasePermission):

    def has_permission(self, request, view):
        if request.user.IsAuthenticated():
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        
        if request.user.is_superuser:
            return True
        elif request.user == obj.author_user_id:
            return True
        else:
            return False


class Is_user_contributor(BasePermission):

    def has_permission(self, request, view):
        if self.request.user.IsAuthenticated():
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif models.Contributor.objects.filter(project_id=obj.id, user_id=request.user).exists:
            return True
        else:
            return False