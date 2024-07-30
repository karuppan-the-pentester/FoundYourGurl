"""
URL configuration for FUG project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('admission_page/',views.admission_page, name='Admission_page'),
    path('students-portal/',views.student_portal, name='students_portal'),
    path('students_dashboard/',views.students_dashboard, name='students_dashboard'),
    path('signout/',views.SignoutPage, name='signout'),
    path('notes/',views.admission_page, name='notes'),
    path('gallery-stud/',views.admission_page, name='gallery-stud'),
    path('id-card/<int:u_id>',views.id_card, name='id_card'),

]
