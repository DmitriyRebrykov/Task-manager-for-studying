from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.ProjectsListView.as_view(), name='projects-list'),
    path('create/', views.ProjectCreationView.as_view(), name='project-create'),
]