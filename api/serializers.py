from Events import models as event_models
from users import models as user_models
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username",]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_models.Profile
        fields="__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=event_models.Comments
        fields="__all__"

class EventSerializer(serializers.ModelSerializer):
    # comment = CommentSerializer(source="comments", many=True)
    class Meta:
        model = event_models.Event
        fields = ["pk",'title', 'description', 'event_img','event_date',
				  'event_location','open_slot',
				  'categories'
				 ]

class CategoryDetailSerializer(serializers.ModelSerializer):
    events = EventSerializer(source='category', many=True)
    class Meta:
        model = event_models.Category
        fields=["name", "id", "events",]
