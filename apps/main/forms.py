from django import forms

from apps.main.models import Project, Task


class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Work Projects'}),
        }

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control task-input', 'placeholder': 'Start typing...'}),
        }