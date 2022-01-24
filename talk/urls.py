from django.urls import path
from .views import dashboard

app_name = "talk"

urlpatterns = [
    path("", dashboard, name="dashboard"),
]