from django.urls import path
from .views import RegistrationView, LoginView

urlpatterns = [
    path('api/registration/', RegistrationView.as_view()),
    path('api/login/', LoginView.as_view())
]
