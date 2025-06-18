from django.urls import path
from . import views

app_name = 'malayalam'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('python/1/', views.python_chapter_1, name='python-1'),
    path('python/2/', views.python_chapter_2, name='python-2'),
]