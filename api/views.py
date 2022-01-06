from rest_framework import viewsets
from . import serializers
from . import models
from rest_framework.permissions import IsAuthenticated

class UserViewset(viewsets.ModelViewSet):
    
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    #permission_classes = [IsAuthenticated]



class ProjectViewSet(viewsets.ModelViewSet):

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    #permission_class = [IsAuthenticated]
   

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author"] = request.user.pk
        request.POST._mutable = False
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author"] = request.user.pk
        request.POST._mutable = False
        return super().update(request, *args, **kwargs)

    
class ContributorViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ContributorSerilizer

    def get_queryset(self, *args, **kwargs):
        project_pk = self.kwargs.get('project_pk')
        return models.Contributor.objects.filter(project_id =project_pk)

    def create(self, request, *args, **kwargs):
        project_pk = self.kwargs.get('project_pk')
        request.POST._mutable = True
        request.data["project_id"] = project_pk
        request.POST._mutable = False
        return super().create(request, *args, **kwargs)


class IssueViewSet(viewsets.ModelViewSet):

    serializer_class =serializers.IssueSerializer
    queryset = models.Issue.objects.all()

    def get_queryset(self, *args, **kwargs):
        project_pk = self.kwargs.get('project_pk')
        return models.Issue.objects.filter(project_id =project_pk)

    def create(self, request, *args, **kwargs):
        project_pk = self.kwargs.get('project_pk')
        request.POST._mutable = True
        request.data["project_id"] = project_pk
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super().create(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()

    def get_queryset(self, *args, **kwargs):
        issue_pk = self.kwargs.get('issue_pk')
        return models.Comment.objects.filter(issue_id =issue_pk)

    def create(self, request, *args, **kwargs):
        issue_pk = self.kwargs.get('issue_pk')
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.data["issue_id"] = issue_pk
        request.POST._mutable = False
        return super().create(request, *args, **kwargs)