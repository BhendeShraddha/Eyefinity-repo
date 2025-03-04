from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import IsDoctor


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class PatientListView(APIView):
    permission_classes = [IsDoctor]

    def get(self, request):
        patients = ["Patient 1", "Patient 2", "Patient 3"]
        return Response({"patients": patients})
