from django.views.generic import ListView

from apps.main.models import Project


class ProjectsListView(ListView):
    model = Project
    template_name = 'main/main.html'
    context_object_name = 'projects'
