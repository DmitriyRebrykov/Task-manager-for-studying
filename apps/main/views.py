from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DeleteView, UpdateView

from apps.main.models import Project, Task
from apps.main.forms import ProjectCreationForm, TaskCreationForm
from django.contrib import messages


class ProjectsListView(ListView):
    model = Project
    template_name = "main/main.html"
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProjectCreationForm()
        context["task_form"] = TaskCreationForm()
        return context


class ProjectCreationView(FormView):
    model = Project
    template_name = "main/main.html"
    form_class = ProjectCreationForm
    success_url = reverse_lazy("main:projects-list")

    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()

        messages.success(self.request, "Project created successfully")
        return super().form_valid(form)


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "main/main.html"
    form_class = ProjectCreationForm
    success_url = reverse_lazy("main:projects-list")

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, "Project was updated successfully")
        return super().form_valid(form)


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("main:projects-list")

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, "Project deleted successfully")
        return super().form_valid(form)


class TaskCreationView(FormView):
    model = Task
    template_name = "main/main.html"
    form_class = TaskCreationForm
    success_url = reverse_lazy("main:projects-list")

    def form_valid(self, form, *args, **kwargs):
        print(form.cleaned_data)
        print(self.kwargs)
        task = form.save(commit=False)
        task.project_id = self.kwargs["pk"]
        form.save()

        messages.success(self.request, "Task created successfully")
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "main/main.html"
    form_class = TaskCreationForm
    success_url = reverse_lazy("main:projects-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("main:projects-list")

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, "Task was deleted successfully")
        return super().form_valid(form)
