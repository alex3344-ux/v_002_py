from django.forms import ModelForm
from .models import Student


class StudentAddForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        
    