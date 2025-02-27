"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index
from .htmx_views import *

urlpatterns = [
    path('', index, name='home'),
]

htmxurlpatterns = [
    path('check-status/', check_status, name='check_status'),
    path('check-conclusion/', check_conclusion, name='check_conclusions'),
    path('check-created-at/', check_created_at, name='created_at'),
    path('check-updated-at/', check_updated_at, name='updated_at'),
]

urlpatterns += htmxurlpatterns