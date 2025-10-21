from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('template/', views.template, name='template_page'),
    path('build/<str:name>/', views.build_page, name='build_page'),
]
