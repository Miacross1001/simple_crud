"""simple_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from measurements.views import ProjectViewSet, MeasurementViewSet

# TODO: настройте роутер и подключите `ProjectViewSet` и `MeasurementViewSet`

urlpatterns = [
    path('admin/', admin.site.urls),

    path('project/', ProjectViewSet.as_view({'get': 'list'})),
    path('project/create', ProjectViewSet.as_view({'put': 'create'})),
    path('project/<int:pk>', ProjectViewSet.as_view({'put': 'update'})),
    path('project/delete/<int:pk>', ProjectViewSet.as_view({'delete': 'destroy'})),

    path('measurement/', MeasurementViewSet.as_view({'get': 'list'})),
    path('measurement/create', MeasurementViewSet.as_view({'put': 'create'})),
    path('measurement/<int:pk>', MeasurementViewSet.as_view({'put': 'update'})),
    path('measurement/delete/<int:pk>', MeasurementViewSet.as_view({'delete': 'destroy'})),
]
