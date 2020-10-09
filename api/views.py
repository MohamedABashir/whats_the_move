from django.contrib.auth import get_user_model
from rest_framework import generics, status, viewsets
from rest_framework import permissions as p
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.shortcuts import get_object_or_404

from Events.models import Category, Event, Comments
from users.models import Profile


from .permissions import IsAuthorOrReadOnly
from .serializers import (CategoryDetailSerializer, EventSerializer,
                          ProfileSerializer, UserSerializer)
class CategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

class EventView(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly & (p.IsAuthenticatedOrReadOnly)]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
            file_serializer = EventSerializer(data=request.data)
            if file_serializer.is_valid():
                    file_serializer.save()
                    return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
                    return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileView(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserListView(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
@api_view(["POST"])
@permission_classes([p.IsAuthenticated])
def join_event(request, eventid):
    event = Event.objects.get(id=eventid)
    if event.not_expired() and event.open_slot>0:
        event.attend.add(request.user)
        event.open_slot-=1
        return Response({"message": "Added to the event"})
    return Response({"message": "failed to be added"})
