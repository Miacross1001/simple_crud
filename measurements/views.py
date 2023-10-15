from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from .models import Project, Measurement
from .serializers import ProjectSerializer, MeasurementSerializer


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def destroy(self, request, pk):
        item = get_object_or_404(Project.objects.all(), pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()

    def destroy(self, request, pk):
        item = get_object_or_404(Measurement.objects.all(), pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
