from django import forms
from .models import comment


class CommentForm(forms.Form):
    class Meta:
        model = comment
        fields = ('name', 'email', 'comment')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        pass

    pass

    def save(self, commit):
        pass
