

from django.urls import path
from . import views

urlpatterns = [
  path('', views.super_methods),
  path('<int:pk>/', views.super_by_id)
]