from django.urls import path
from .views import (
		category_detail, 
		explore, 
		EventCreateView, 
		EventDetailView, 
		event_map,
		join_event,
		EventUpdateView,
		EventDeleteView)

urlpatterns = [
	path('', explore, name='explore' ),
	path('category/<str:cats>/', category_detail, name='category-detail'),	
	path('events/<str:cats>/<slug:slug>/<int:pk>/', EventDetailView.as_view(), name='event-detail'),	
	path('events/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
	path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),		
	path('events/new/', EventCreateView.as_view(), name='create-event'),
	path('explore/map/', event_map, name='event-map'),
	path('attend/<int:pk>/', join_event, name='join_event'),

]