from django.contrib import admin
from website.models import *

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('name', 'email', 'created_date')
    search_fields = ('name', 'email', 'message')