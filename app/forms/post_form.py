from django import forms
from ..models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'status', 'corpo']
        widgets = {
            'titulo': forms.TextInput(),
            'status': forms.Select(),
            'corpo': forms.Textarea()
        }

        help_texts = {
            'titulo': 'Informe um titulo',
            'status': 'Selecione o status',
            'corpo': 'Escreva um corpo',
        }