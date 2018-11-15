from django.contrib import admin
from .models import Sigudong


class SigudongAdmin(admin.ModelAdmin):
	list_display = ('si', 'gu', 'dong')

admin.site.register(Sigudong, SigudongAdmin)
