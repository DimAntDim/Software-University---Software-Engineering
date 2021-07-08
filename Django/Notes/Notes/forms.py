from django import forms
from .models import Note

class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class EditNoteForm(AddNoteForm):
    pass


class DeleteNoteForm(forms.ModelForm):
    title = forms.CharField(disabled=True)
    image_url = forms.URLField(disabled=True)
    content = forms.CharField(widget=forms.TextInput, disabled=True)
    class Meta:
        model = Note
        fields = '__all__'