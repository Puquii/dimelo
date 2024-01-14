from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit, name='submit'),
    path('', views.index, name = 'index'),
]