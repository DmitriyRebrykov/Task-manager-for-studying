from django import forms
from django.utils import timezone

from apps.main.models import Project, Task


class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g. Work Projects"}
            ),
        }


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "deadline"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control task-input",
                    "placeholder": "Start typing...",
                }
            ),
            "deadline": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "done": forms.CheckboxInput(attrs={"class": "custom-check"}),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline and deadline < timezone.now():
            raise forms.ValidationError("Deadline cannot be in the past.")
        return deadline
