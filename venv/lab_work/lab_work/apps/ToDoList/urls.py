# app URLs
from django.urls import path
from . import views

app_name = 'ToDoList'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:exercise_id>/', views.detail, name = 'detail'),
    path('delete/<int:pk>/', views.delete, name = 'delete'),
    path('create/', views.create, name = 'create'),
    path('<int:pk>/edit/', views.edit, name = 'edit'),
]