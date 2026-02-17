from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.ProjectsListView.as_view(), name='projects-list'),
    path('projects/create/', views.ProjectCreationView.as_view(), name='project-create'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project-delete'),

    path('projects/<int:pk>/task/create/', views.TaskCreationView.as_view(), name='task-create'),
]