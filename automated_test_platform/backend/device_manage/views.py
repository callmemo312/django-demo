import re
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import StudentForm
from django import forms

from .models import Student
from django.views import View

# Create your views here.
# def index(request):
#     students = Student.objects.all()
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             student = Student()
#             student.name = cleaned_data['name']
#             student.sex = cleaned_data['sex']
#             student.email = cleaned_data['email']
#             student.profession = cleaned_data['profession']
#             student.qq = cleaned_data['qq']
#             student.phone = cleaned_data['phone']
#             student.save()
#             return HttpResponseRedirect(reverse('index'))
#     else:
#         form = StudentForm()

#     context = {
#         'students': students,
#         'form': form
#     }    
#     return render(request, 'index.html', context=context)


class IndexView(View):
    def get_context(self):
        students = Student.objects.all()
        context = {
            'students': students 
        }
        return context
    
    def get(self, request):
        context = self.get_context()
        context.update({
            'form': StudentForm()
        })
        return render(request, 'index.html', context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            raise forms.ValidationError('参数格式错误！')