from django.contrib import admin

#relative import-admin and models are in the same app
from .models import Event 

admin.site.register(Event)
