from django.urls import path
from . import views

app_name = 'malayalam'

urlpatterns = [
    path('', views.home, name='home'),
]