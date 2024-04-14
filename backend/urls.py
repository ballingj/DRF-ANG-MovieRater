from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet, GroupViewSet

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-api/', include(router.urls)),
    path('api/', include("backend.api.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', obtain_auth_token),
]

# Customize the Admin Page
admin.site.site_title = "Movie Rating site admin (DEV)"
admin.site.site_header = "Movie Rating administration"
admin.site.index_title = "Movie administration"
