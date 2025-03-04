from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet  # ✅ Import only what's needed
from .views import PatientListView

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)  # ✅ Direct import avoids circular issues

urlpatterns = [
    path('', include(router.urls)),
    path('patients/', PatientListView.as_view(), name='patients-list'),
]
