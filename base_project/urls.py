"""Base_Project URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('', include('base_project.apps.accounts.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi/', get_schema_view(
        title="Base_Project",
        description="API for Base_Project",
        version="0.0.0"
    ), name='openapi-schema'),
]
