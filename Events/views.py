from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages

from .models import Category, Event
from .forms import EventForm
import folium
import geocoder
import os
import datetime
import pytz


def explore(request):
	cat = Category.objects.all()
	context = {'categories':cat, 'title':"Explore"}
	return render(request, 'Events/explore.html', context)

def get_icon_option(cat_name, choice):
	icon_option = {
		'Tech': {'color': 'red', 'icon': 'desktop'},
		'Family': {'color': 'purple', 'icon': 'slideshare'},
		'Health & Wellness': {'color': 'pink', 'icon': 'user-md'},
		'Sports & Fitness': {'color': 'orange', 'icon': 'soccer-ball-o'},
		'Learning': {'color': 'lightred', 'icon': 'university'},
		'Photography': {'color': 'lightgreen', 'icon': 'camera'},
		'Food & Drink': {'color': 'lightgray', 'icon': 'cutlery'},
		'Writing': {'color': 'lightblue', 'icon': 'pencil'},
		'Language & Culture': {'color': 'green', 'icon': 'language'},
		'Music': {'color': 'gray', 'icon': 'music'},
		'Movements': {'color': 'darkred', 'icon': 'resistance'},
		'Film': {'color': 'darkpurple', 'icon': 'film'},
		'Sci-Fi & Games': {'color': 'darkgreen', 'icon': 'gamepad'},
		'Beliefs': {'color': 'darkblue', 'icon': 'balance-scale'},#
		'Arts': {'color': 'cadetblue', 'icon': 'paint-brush'},
		'Book Clubs': {'color': 'blue', 'icon': 'leanpub'},
		'Dance': {'color': 'black', 'icon': 'child'},#
		'Pets': {'color': 'beige', 'icon': 'paw'},
		'Hobbies & Crafts': {'color': 'blue', 'icon': 'code'},
		'Fashion & Beauty': {'color': 'black', 'icon': 'black-tie'},#
		'Social': {'color': 'beige', 'icon': 'plug'},
		'Career & Business': {'color': 'blue', 'icon': 'piggy-bank'},
		'Outdoors & Adventure': {'color': 'red', 'icon': 'map '}
	}
	return icon_option[cat_name].get(choice	)	
def event_map(request):
	m = folium.Map([45.055328,-93.239918], zoom_start=10,padding_top_left=(100,100))
	e = Event.objects.all()
	e = [i for i in e if i.event_date> datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)]
	for i in e:
		some = f""" 
			<div class="card" style="width: 18rem;">
			  <img class="card-img-top" style="width:100%"src="{i.event_img.url}" alt="Card image cap">
			  <div class="card-body">
			    <h5 class="card-title">{i.title}</h5>
			    <div class="row">
		    	<div class="column">
                <img style="border-radius: 50%;width:2em; height: 2em" src="{i.host.profile.img.url}" class="user"/>
              	</div>
			    <p class="card-text column">{i.host}</p>
			    <a href="{i.get_absolute_url()}" target="_parent"class="btn btn-primary">More Detail</a>
			  	</div>
			  </div>
			</div>
		"""
		# print()
		test = folium.Html(some, script=True)
		popup = folium.Popup(test, max_width=200,  parse_html=True)
		latlng = [i.event_location[0],i.event_location[1]]
		try:
			latlng = [latlng[1], latlng[0]]
		except:
			latlng = [latlng[0], latlng[1]]

		folium.Marker(
			location=latlng,
			tooltip="Click for info", 
			popup=popup, 
			icon=folium.Icon(color=get_icon_option(i.categories.name,"color"),
			icon=get_icon_option(i.categories.name,"icon"),prefix='fa')
		).add_to(m)
	m=m._repr_html_() #updated
	context = {'my_map': m, 'title':"Map"}
	return render(request, 'Events/maps.html', context)
def category_detail(request, cats):
	event_category = Category.objects.filter(slug=cats).first()
	return render(request, 'Events/category_detail.html',
	 {'event_category':event_category, 'title':'Category'})

def join_event(request,pk):
	event = get_object_or_404(Event, id=request.POST.get('event_pk'))
	if event.not_expired() and event.open_slot>0:
		event.attend.add(request.user)
		event.open_slot-=1
		messages.success(request, f'Request was a success!')
	return HttpResponseRedirect(event.get_absolute_url())


class EventCreateView(CreateView):
	model = Event
	form_class = EventForm
	def form_valid(self, form):
		form.instance.host = self.request.user
		super().form_valid(form)
		form.instance.attend.add(self.request.user)
		return super().form_valid(form)

class EventUpdateView(UserPassesTestMixin, UpdateView):
	model = Event
	form_class = EventForm
	def form_valid(self, form):
		form.instance.host = self.request.user
		return super().form_valid(form)
	def test_func(self):
		event = self.get_object()
		if self.request.user == event.host:
			return True
		return False


class EventDeleteView(UserPassesTestMixin, DeleteView):
	model = Event
	success_url = '/'
	def test_func(self):
		event = self.get_object()
		if self.request.user == event.host:
			return True
		return False


class EventDetailView(DetailView):
	model = Event
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		latlng = context['event'].event_location
		event = get_object_or_404(Event, id=self.kwargs['pk'])
		attendees = event.number_of_attendees()
		try:
			latlng = [latlng[1], latlng[0]]
			g = geocoder.mapbox(latlng, method='reverse', key=os.environ.get('MAPBOX_API_KEY'))
		except ValueError as e :
			print(e)
			latlng = context['event'].event_location
			g = geocoder.mapbox(latlng, method='reverse', key=os.environ.get('MAPBOX_API_KEY'))

		context['attendees'] = attendees
		context['location_name'] = str(g.current_result).replace('[', '').replace(']', '')
		return context
