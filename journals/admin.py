from django.contrib import admin
from .models import Title, Entry


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'date_created', 'date_updated')
    

class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'date_created', 'date_updated')


admin.site.register(Title, TitleAdmin)
admin.site.register(Entry, EntryAdmin)
