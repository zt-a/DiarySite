from django import forms
from .models import *


class AddDiaryForm(forms.ModelForm):
    class Meta:
        model = DiaryModel
        fields = ['content', ]
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control add-input',
                'name': 'field',
                'id': 'field',

            }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['is_published'].reqired = False
        # self.fields['is_published'].initial = True


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = NotesModel
        fields = ['title', 'slug', 'content', 'is_published', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 10}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['is_published'].reqired = False
        self.fields['is_published'].initial = True


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ['name', 'title', 'slug', 'content', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control nameContact'}),
            'title': forms.TextInput(attrs={'class': 'form-control titleContact'}),
            'slug': forms.TextInput(attrs={'class': 'form-control slugContact'}),
            'content': forms.Textarea(attrs={'class': 'form-control contentContact', 'cols': 60, 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
