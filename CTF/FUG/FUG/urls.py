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

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('admission_page/',views.admission_page, name='Admission_page'),
    path('students-portal/',views.student_portal, name='students_portal'),
    path('students_dashboard/',views.students_dashboard, name='students_dashboard'),
    path('gallery/',views.Gallery, name='gallery'),
    path('signout/',views.SignoutPage, name='signout'),
    path('notes/',views.notes, name='notes'),
    path('notes/view-notes/<int:notes_id>',views.view_notes, name='view_notes'),
    path('gallery-stud/',views.gallery_stud, name='gallery-stud'),
    path('upload/', views.image_upload_view, name='upload'),
    path('id-card/<int:u_id>',views.id_card, name='id_card'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)