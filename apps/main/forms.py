from django import forms

from apps.main.models import Project


class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Work Projects'}),
        }


