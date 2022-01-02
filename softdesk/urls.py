from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api import views
from auth.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = SimpleRouter()
router.register('user', views.UserViewset, basename='user')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_tokens'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/', include(router.urls)),
]


