from django.contrib import admin
from . import models
@admin.register(models.Divar)
class Divar(admin.ModelAdmin):
        list_display = ('Category','Ad_Titel','Description','City','status','price','Phone','Author','Date','slug')
        list_filter  = ('Category','City','status','price','Author','Date','slug')
