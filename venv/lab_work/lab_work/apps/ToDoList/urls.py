# app URLs
from django.urls import path
from . import views

app_name = 'ToDoList'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:exercise_id>', views.detail, name = 'detail'),
    path('<int:pk>/delete-item', views.delete, name = 'delete'),
    path('create-item/', views.create, name = 'create'),
    path('<int:pk>/edit-item', views.edit, name = 'edit'),
]