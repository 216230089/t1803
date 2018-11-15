from django.contrib import admin
from .models import Emer,City


class CityAdmin(admin.ModelAdmin):
	list_display = ('si', 'gu', 'dong')

admin.site.register(City, CityAdmin)

class EmerAdmin(admin.ModelAdmin):
	list_display = ('mname', 'madd', 'mtel')
	search_fields = ('mname', 'madd', 'mtel')
	

admin.site.register(Emer, EmerAdmin)

