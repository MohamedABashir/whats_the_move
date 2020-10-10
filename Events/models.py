import datetime

import pytz
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django_comments_xtd.models import XtdComment
from django_comments_xtd.signals import should_request_be_authorized
from mapbox_location_field.models import AddressAutoHiddenField, LocationField
from PIL import Image
from tinymce import HTMLField

# from django.utils.text import slugify 
from .uniqueslug import unique_slugify


class Category(models.Model):
	name = models.CharField(max_length=70)
	slug = models.CharField(max_length=70)
	class Meta:
		verbose_name_plural = "Categories"
	def __str__(self):
		return self.name

		

class Event(models.Model):
	host = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=70)
	description = HTMLField("Description")
	event_img = models.ImageField(upload_to='event_pics')
	event_date = models.DateTimeField()
	event_location = LocationField()
	categories = models.ForeignKey(Category, default=1, verbose_name = "Categories", related_name="category",on_delete=models.SET_DEFAULT)
	slug = models.SlugField(blank=True)
	attend = models.ManyToManyField(User, related_name='attendees',blank=True, default=None)
	open_slot = models.IntegerField(default=5,null=True)
	# comments = models.ManyToManyField(Comments, blank=True, verbose_name = "comment", 
	# 						related_name="comments")
	

	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('event-detail', kwargs={'cats':self.categories.slug, 'slug':self.slug})
	def number_of_attendees(self):
		return self.attend.all().count
	def not_expired(self):
		return self.event_date > datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
	def save(self, **kwargs):
	    slug_str = "%s" % (self.title) 
	    unique_slugify(self, slug_str) 
	    super(Event, self).save(**kwargs)

class Comments(XtdComment):
	def save(self, *args, **kwargs):
		if self.user:
			self.user_name = self.user.username
		super(Comments, self).save(*args, **kwargs)
	def __str__(self):
		return self.comment
	def event_url(self):
		x = self.content_object.id
		event = Event.objects.filter(id=x).first()
		return event.get_absolute_url()



@receiver(should_request_be_authorized)
def my_callback(sender, comment, request, **kwargs):
    if (
        (request.user and request.user.is_authenticated)
    ):
        return True
