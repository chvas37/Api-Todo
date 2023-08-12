from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'not_done', 'in_process', 'done')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description')
    list_editable = ('not_done', 'in_process', 'done',)
    list_filter = ('not_done', 'in_process', 'done',)


admin.site.register(Todo, TodoAdmin)
