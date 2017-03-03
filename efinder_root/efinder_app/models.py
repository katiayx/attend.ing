from __future__ import unicode_literals
from django.conf import settings

from django.db import models

# class EventManager(models.Manager):





class Event(models.Model):
	"""Events"""

	event_name	= models.CharField(max_length=220)
	description = models.TextField()
	start_time	= models.CharField(max_length=50)
	end_time	= models.CharField(max_length=50)
	url 		= models.CharField(max_length=200)
	is_free		= models.BooleanField(default=False)
	updated		= models.DateTimeField(auto_now=True)

	# objects = EventManager()

	def __unicode__(self):
		return self.event_name




