from django.contrib import admin
from .models import *

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'time_create', 'content')
    search_fields = ('id', 'time_create', 'time_update', 'content', 'is_published')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'time_create')
    # prepopulated_fields = {'slug': ('time_create')}

class NotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'slug', 'time_create', 'content')
    search_fields = ('id', 'title', 'slug', 'time_create', 'time_update', 'content', 'is_published')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(DiaryModel, DiaryAdmin)
admin.site.register(NotesModel, NotesAdmin)
admin.site.register(ContactUsModel)

