from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(BaseModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["name"]


class Task(BaseModel):
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return f"Task {self.name} for {self.project}"

    def clean(self):
        super().clean()

        from django.utils import timezone

        if self.deadline and self.deadline < timezone.now():
            raise ValidationError({"deadline": ("Date cannot be")})

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["order", "name"]
