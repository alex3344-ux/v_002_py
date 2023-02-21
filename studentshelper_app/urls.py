from django.urls import path
from .views import show_studentshelper

app_name = "studentshelper_app"

urlpatterns = [
    path("", show_studentshelper, name="show_studentshelper"),
]
