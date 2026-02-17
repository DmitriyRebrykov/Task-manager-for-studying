from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from apps.main.models import Project
from apps.main.forms import ProjectCreationForm

class ProjectsListView(ListView):
    model = Project
    template_name = 'main/main.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectCreationForm()
        return context


class ProjectCreationView(FormView):
    model = Project
    template_name = 'main/main.html'
    form_class = ProjectCreationForm
    success_url = reverse_lazy('main:projects-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        return super().form_valid(form)