from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_tasks, name='get_all_tasks'),
    path('<int:pk>/', views.get_task_by_id, name='get_task_by_id'),
    path('<int:pk>/update/', views.update_task, name='update_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('create/', views.create_task, name='create_task'),
]
