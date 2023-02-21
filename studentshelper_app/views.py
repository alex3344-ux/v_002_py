from django.shortcuts import render
from studentshelper_app.models import Studentshelper


# Create your views here.

def show_studentshelper(request) -> render:
    template_ = 'studentshelper.html'
    subjects = Studentshelper.objects.all()

    context = {
        'subjects': subjects,
    }

    return render(request=request, template_name=template_, context=context)


