from django.urls import path
from .views import CategoryView, EventView, ProfileView,UserListView,join_event,CommentList
from rest_framework import routers

urlpatterns = [
    path('join/<int:eventid>/',join_event),
    path('user-comments/<int:userid>/',CommentList.as_view()),

]

router = routers.DefaultRouter()
router.register(r'category', CategoryView)
router.register(r'event', EventView)
router.register(r'profile', ProfileView)
router.register(r'user', UserListView)





urlpatterns += router.urls