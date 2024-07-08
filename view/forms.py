from django import forms
from onenote.models import Note

class NoteForm(forms.ModelForm):
    """Form definition for Note."""

    class Meta:
        """Meta definition for Noteform."""

        model = Note
        fields = ['title','who','count','body']
