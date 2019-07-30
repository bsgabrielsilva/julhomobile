from django import forms
from ..models import Comments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment', 'post']
        widgets = {
            'comment': forms.Textarea(),
            'post': forms.TextInput(attrs={'type': 'hidden'})
        }

        help_texts = {
            'comment': 'Comente baboseira',
        }


class CommentsAdminForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment', 'autorizado', 'post']
        widgets = {
            'comment': forms.Textarea(),
            'autorizado': forms.CheckboxInput(),
            'post': forms.TextInput(attrs={'type': 'hidden'})
        }

        help_texts = {
            'comment': 'Comente baboseira',
            'autorizado': 'Autoriza o comentário?'
        }