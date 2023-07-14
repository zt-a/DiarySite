from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('diary/', DiaryPage, name='diary_page'),
    # path('diaries/<id:id>/', DiaryPost, name='diary_post'),
    path('notes/', NotesPage, name='notes_page'),
    path('addnotes/', addNotes, name='add_notes_page'),
    path('contactUs/', contactUs, name='contactUs'),
    path('aboutUs/', aboutUs, name='aboutUs'),
]
