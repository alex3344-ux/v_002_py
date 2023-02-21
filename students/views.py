from django.shortcuts import render, get_object_or_404
from .models import Student, Group

from django.db.models import Q, F, Count
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from .forms import StudentAddForm

from icecream import ic



# Create your views here.


def students_view(request, pk=None) -> render:
    template_ = "students_all.html"
    if pk:
        template_ = "student_detail.html"
        student = get_object_or_404(Student, pk=pk)
        context = {"student": student}
    else:
        groups = Group.objects.all()
        students = Student.objects.select_related("group").all()

        max_cols = 0

        for group_item in groups:
            students_len = len(Student.objects.select_related('group').filter(Q(group=group_item.pk)))

            if max_cols < students_len:
                max_cols = students_len

        context = {
            "students": students,
            "groups": groups,
            "max_cols": max_cols,
        }
    return render(request=request, template_name=template_, context=context)

        
class StudentTempateView(TemplateView):
    template_name = "student_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "student": get_object_or_404(Student, pk=self.kwargs["pk"])
        }
        return context
    
class StudentAddView(CreateView):
    model = Student
    template_name = "student_add.html"
    success_url = "/students/"
    form_class = StudentAddForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save(commit=True)  
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
