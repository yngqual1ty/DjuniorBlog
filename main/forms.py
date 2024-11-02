from django.template.defaultfilters import title

from .models import Publication
from django.forms import ModelForm, Textarea, TextInput, DateInput


class CreateBlogForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'shortDescription', 'content']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок публикации'}),
            'shortDescription': Textarea(attrs={'class': 'form-control', 'placeholder': 'Короткое описание'}),
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст публикации'}),
        }

class EditBlogForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'shortDescription', 'content']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'shortDescription': Textarea(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control'}),
        }