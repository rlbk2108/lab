# app URLs
from django.urls import path
from . import views

app_name = 'ToDoList'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:exercise_id>/', views.TaskDetail, name = 'detail'),
]