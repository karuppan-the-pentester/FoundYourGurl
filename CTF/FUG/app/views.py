from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def admission_page(request):
    return render(request, 'Admission_page.html')

def student_portal(request):
    return render(request, 'student-portal.html')