from django.urls import path

from .views import task_delete, task_list, task_done

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task_delete/<int:task_id>/', task_delete, name='task_delete'),
    path('task_done/<int:task_id>/', task_done, name='task_done'),
]