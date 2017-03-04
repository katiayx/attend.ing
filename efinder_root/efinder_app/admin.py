from django.contrib import admin

#relative import-admin and models are in the same app
from .models import Event 

class EventModelAdmin(admin.ModelAdmin):
	list_display = ('event_name', 'start_time', 'register_url', 'is_free')
	list_display_links = ['start_time']
	list_filter = ('start_time', 'is_free')
	search_fields = ('event_name', 'is_free')
	class Meta:
		model = Event



admin.site.register(Event, EventModelAdmin)
