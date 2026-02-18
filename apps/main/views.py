import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, DeleteView, UpdateView

from apps.main.models import Project, Task
from apps.main.forms import ProjectCreationForm, TaskCreationForm
from django.contrib import messages


class ProjectsListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "main/main.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user).prefetch_related("tasks")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProjectCreationForm()
        context["task_form"] = TaskCreationForm()
        return context


class ProjectCreationView(LoginRequiredMixin, FormView):
    model = Project
    template_name = "main/main.html"
    form_class = ProjectCreationForm
    success_url = reverse_lazy("main:projects-list")

    def form_valid(self, form):
        project = form.save(commit=False)
        project.user = self.request.user
        project.save()
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
        task = form.save(commit=False)
        task.project_id = self.kwargs["pk"]
        task.save()

        if self.request.headers.get("HX-Request"):
            return render(self.request, "main/partials/task_item.html", {"task": task})

        messages.success(self.request, "Task created successfully")
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "main/main.html"
    form_class = TaskCreationForm
    success_url = reverse_lazy("main:projects-list")

    def form_valid(self, form):
        task = form.save()

        if self.request.headers.get("HX-Request"):
            return render(self.request, "main/partials/task_item.html", {"task": task})

        messages.success(self.request, "Task updated successfully")
        return super().form_valid(form)


class TaskDeleteView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()

        if request.headers.get("HX-Request"):
            return HttpResponse("")

        messages.success(request, "Task was deleted successfully")
        return redirect("main:projects-list")


class TaskToggleView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()

        if request.headers.get("HX-Request"):
            return render(request, "main/partials/task_item.html", {"task": task})

        return redirect(request.META.get("HTTP_REFERER", "/"))


class TaskReorderView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        for index, item in enumerate(data):
            Task.objects.filter(pk=item["id"]).update(order=index)
        return JsonResponse({"status": "ok"})
