from django.http import request
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import serializers
from . import models
from . import permissions
from itertools import chain

class UserViewset(viewsets.ModelViewSet):
    
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ProjectSerializer
    #permission_classes = [permissions.Project_permission]

    def get_queryset(self):
        queryset1 = models.Project.objects.filter(author_user_id=self.request.user)
        contributors = models.Contributor.objects.filter(user_id=self.request.user)
        list = []
        for contributor in contributors:
            print(contributor.project_id)
            list.append(contributor.project_id)
        queryset2 = models.Project.objects.filter(author_user_id__in=list)
        queryset = queryset1 | queryset2
        return queryset

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super().update(request, *args, **kwargs)
   
    
class ContributorViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ContributorSerializer

    permission_classes = [permissions.Contributor_permission]
    #permissions ==> get: if user == contributor
    #                create, update, destroy: user == project_author

    def get_queryset(self, *args, **kwargs):
        project_pk = self.kwargs.get('project_pk')
        return models.Contributor.objects.filter(project_id =project_pk)

    def create(self, request, *args, **kwargs):
        project_pk = self.kwargs.get('project_pk')
        request.POST._mutable = True
        request.data["project_id"] = project_pk
        request.POST._mutable = False
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        project_pk = self.kwargs.get('project_pk')
        request.POST._mutable = True
        request.data["project_id"] = project_pk
        request.POST._mutable = False
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_pk')
        if self.request.user == user_id:
            print('utiliser drf error pour raise lerreur')
        return super().destroy(request, *args, **kwargs)

    #def destroy vérifier que le user n'est pas nous même 


class IssueViewSet(viewsets.ModelViewSet):

    serializer_class =serializers.IssueSerializer
    queryset = models.Issue.objects.all()
    permission_classes = [IsAuthenticated]
    #permission = get et create: if user == project author ou contributor
    #              update: if user == author

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

    def update(self, request, *args, **kwargs):
        project_pk = self.kwargs.get('project_pk')
        request.POST._mutable = True
        request.data["project_id"] = project_pk
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super().update(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [IsAuthenticated]
    #permissions ==> get: if user == contributor
    #                reste: if user == author

    def get_queryset(self, *args, **kwargs):
        issue_pk = self.kwargs.get('issues_pk')
        return models.Comment.objects.filter(issue_id =issue_pk)

    def create(self, request, *args, **kwargs):
        issue_pk = self.kwargs.get('issues_pk')
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.data["issue_id"] = issue_pk
        request.POST._mutable = False
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        issue_pk = self.kwargs.get('issues_pk')
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.data["issue_id"] = issue_pk
        request.POST._mutable = False
        return super().update(request, *args, **kwargs)

