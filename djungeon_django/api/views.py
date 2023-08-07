from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    RoomSerializer,
    RoomCreateSerializer,
    ChoiceCreateSerializer,
)
from dungeon.models import Room

class RoomDetail(APIView):
    def get_object(self, room_slug):
        return get_object_or_404(Room, uuid=room_slug)
    
    def get(self, request, room_slug, format=None):
        room = self.get_object(room_slug)
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    
class CreateRoom(APIView):
    def post(self, request):
        data = request.data

        room_data = data.get("room")
        choice1_data = data.get("choice_1")
        choice2_data = data.get("choice_2")

        room_serial = RoomCreateSerializer(data=room_data)
        ch1_serial = ChoiceCreateSerializer(data=choice1_data)
        ch2_serial = ChoiceCreateSerializer(data=choice2_data)

        room_valid = room_serial.is_valid()
        ch1_valid = ch1_serial.is_valid()
        ch2_valid = ch2_serial.is_valid()

        if room_valid and ch1_valid and ch2_valid:
            room = Room.objects.generate(
                name = room_serial.validated_data["name"],
                prompt = room_serial.validated_data["prompt"],
                choice_1_text = ch1_serial.validated_data["text"],
                choice_2_text = ch2_serial.validated_data["text"],
            )
            return Response(room.get_absolute_url(), status=200)
        
        errors = self.combined_errors(
            room_serial.errors,
            ch1_serial.errors,
            ch2_serial.errors,
        )
        return Response(errors, status=400)
    
    def combined_errors(self, room_errors, ch1_errors, ch2_errors):
        errors = {}
        # Room errors
        for key in room_errors:
            errors[key] = room_errors[key][0]
        # Choice 1 errors
        for key in ch1_errors:
            errors["choice 1"] = ch1_errors[key][0]
        # Choice 2 errors
        for key in ch2_errors:
            errors["choice 2"] = ch2_errors[key][0]
        return errors
        
