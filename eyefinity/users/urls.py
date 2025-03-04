# from django.urls import path
# from .views import UserListCreateView

# urlpatterns = [
#     path('users/', UserListCreateView.as_view(), name='user-list-create'),
# ]

from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
