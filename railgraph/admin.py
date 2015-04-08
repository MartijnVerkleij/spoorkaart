from django.contrib import admin
from railgraph.models import Station, Track

# Register your models here.

class StationAdmin(admin.ModelAdmin):
	list_display = ('tel_code','name')

class TrackAdmin(admin.ModelAdmin):
	list_display = ('station_1','station_2')

admin.site.register(Station, StationAdmin)
admin.site.register(Track, TrackAdmin)
