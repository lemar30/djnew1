from django.contrib import admin
from .models import People

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tel')
    list_filter = ('id', 'name', 'tel')
    search_fields = ('id', 'name', 'tel')
# Register your models here.

admin.site.register(People, PeopleAdmin)