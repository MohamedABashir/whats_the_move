from django import forms
from django.forms import ModelForm
from .models import Event, Comments
from django.db import models

class DateInput(forms.DateInput):
    input_type = 'date'


class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ['title', 'description', 'event_img','event_date',
				  'event_location','open_slot',
				  'categories',
				 ]
		widgets = {'event_date':forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', 
								attrs={'class':'datetimefield'})}
		labels = {'event_img':"Event Image", 'title':"Title", 
					'event_date':"Event Date", 'event_location':"Event Location", 
					'open_slot':"Open Slots", "categories":"Categories"}
