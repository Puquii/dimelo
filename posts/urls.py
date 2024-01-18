from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit, name='submit'),
    path('', views.index, name='index'),
    path('description/<slug:slug>/', views.description, name='post_description')
]
