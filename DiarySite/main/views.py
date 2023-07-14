from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import *
from .forms import *


def index(request):
    diary = DiaryModel.objects.filter(is_published=True)
    if request.method == 'POST':
        form = AddDiaryForm(request.POST)
        data = request.POST.get('field')
        request.session['post_data'] = data
    else:
        form = AddDiaryForm()

    if form.is_valid():
        form.save()
        form = AddDiaryForm()
        redirect('home')
    context = {
        'title': 'Главная страница',
        'diaries': diary,
        'form': form,

    }
    return render(request, 'main/index.html', context=context)


class IndexView(CreateView, ListView):
    form_class = AddDiaryForm
    template_name = 'main/index.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


def DiaryPage(request):
    diary = DiaryModel.objects.all()
    context = {
        'title': 'Дневник',
        'diaries': diary,
    }
    return render(request, 'main/diary.html', context=context)


def NotesPage(request):
    notes = NotesModel.objects.filter(is_published=True)
    context = {
        'title': 'Заметки',
        'notes': notes,
    }
    return render(request, 'main/notes.html', context=context)


def addNotes(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
    else:
        form = AddNoteForm()
    if form.is_valid():
        form.save()
        redirect('notes_page')

    context = {
        'title': 'Добавить заметку',
        'form': form,
    }
    return render(request, 'main/add-notes.html', context=context)


def aboutUs(request):
    context = {
        'title': 'О нас',
    }
    return render(request, 'main/aboutUs.html', context=context)


def contactUs(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
    else:
        form = ContactUsForm()
    if form.is_valid():
        form.save()
        redirect('home')

    context = {
        'title': 'Обратная связь',
        'form': form,
    }
    return render(request, 'main/contactUs.html', context=context)
