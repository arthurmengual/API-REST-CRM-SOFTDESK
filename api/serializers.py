from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Comment, Contributor, Issue, Project, User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        include = ['id']

   

class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

class Project_detail_serializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title']

class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = '__all__'



class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
