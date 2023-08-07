from django.urls import path
from .views import (
    RoomDetail,
    CreateRoom,
)

urlpatterns = [
    path("create-room/", CreateRoom.as_view()),
    path("rooms/<slug:room_slug>/", RoomDetail.as_view()),
]
