from django.urls import path
from .views import RegistrationApiView, LoginApiView

app_name = "authentication"
urlpatterns = [
    path("registration/", RegistrationApiView.as_view()),
    path("login/", LoginApiView.as_view()),
]
