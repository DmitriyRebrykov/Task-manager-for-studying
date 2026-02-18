from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    # PROJECTS URLS
    path("", views.ProjectsListView.as_view(), name="projects-list"),
    path(
        "projects/create/", views.ProjectCreationView.as_view(), name="project-create"
    ),
    path(
        "projects/<int:pk>/delete/",
        views.ProjectDeleteView.as_view(),
        name="project-delete",
    ),
    path(
        "projects/<int:pk>/update/",
        views.ProjectUpdateView.as_view(),
        name="project-update",
    ),
    # TASKS URLS
    path(
        "projects/<int:pk>/task/create/",
        views.TaskCreationView.as_view(),
        name="task-create",
    ),
    path(
        "projects/<int:pk>/task/delete/",
        views.TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "projects/<int:pk>/task/update/",
        views.TaskUpdateView.as_view(),
        name="task-update",
    ),
    path("tasks/<int:pk>/toggle/", views.TaskToggleView.as_view(), name="task-toggle"),
]
