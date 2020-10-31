from django.urls import path
from rest_framework import routers

from .views import (AllEventByUser, CategoryView, CommentList, EventView,
                    ProfileView, UserListView, join_event)

urlpatterns = [
    path('join/<int:eventid>/',join_event),
    path('user-comments/<int:userid>/',CommentList.as_view()),
    path('user-events/<int:userid>/',AllEventByUser.as_view()),

]

router = routers.DefaultRouter()
router.register(r'category', CategoryView)
router.register(r'event', EventView)
router.register(r'profile', ProfileView)
router.register(r'user', UserListView)





urlpatterns += router.urls
