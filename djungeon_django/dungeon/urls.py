from django.urls import path
from .views import (
    RoomCreateView,
    RoomDetailView,
)

urlpatterns = [
    path("", RoomCreateView.as_view(), name="room-create"),
    path("<uuid:room_uuid>/", RoomDetailView.as_view(), name="room-detail")
]
