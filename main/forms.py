from django.contrib.auth.forms import UserCreationForm
from django.db.models import TextField
from django.template.defaultfilters import title, length

from .models import Publication, User
from django.forms import ModelForm, Textarea, TextInput, DateInput, PasswordInput


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

class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']

