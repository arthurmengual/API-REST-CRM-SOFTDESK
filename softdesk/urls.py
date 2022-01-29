from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api import views
from auth.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_nested import routers

router = SimpleRouter()
router.register('projects', views.ProjectViewSet, basename='project')

projects_router = routers.NestedSimpleRouter(
    router, 'projects', lookup='project')
projects_router.register('users', views.ContributorViewSet, basename='users')

issues_router = routers.NestedSimpleRouter(
    router, 'projects', lookup='project')
issues_router.register('issues', views.IssueViewSet, basename='issues')

comments_router = routers.NestedSimpleRouter(
    issues_router, 'issues', lookup='issues')
comments_router.register('comments', views.CommentViewSet, basename='comments')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_tokens'),
    path('signup/', RegisterView.as_view(), name='auth_register'),
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('', include(issues_router.urls)),
    path('', include(comments_router.urls)),
]
