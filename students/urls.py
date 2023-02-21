from django.urls import path
from .views import students_view, StudentAddView, StudentTempateView


urlpatterns = [
    path('', students_view, name='students_view'),
    path('<int:pk>/', StudentTempateView.as_view(), name='students_view'),
    path('add', StudentAddView.as_view(), name='student_add'),
]