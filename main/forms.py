from .models import Task
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input task name'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input task description'
            })
            
        }
