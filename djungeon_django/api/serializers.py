from rest_framework import serializers
from dungeon.models import Room, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    room = serializers.UUIDField(source="room.uuid")

    class Meta:
        model = Choice
        fields = (
            "text",
            "room",
        )

class RoomSerializer(serializers.ModelSerializer):
    choice_1 = ChoiceSerializer(allow_null=True)
    choice_2 = ChoiceSerializer(allow_null=True)
    type_class = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = (
            "id",
            "uuid",
            "name",
            "prompt",
            "choice_1",
            "choice_2",
            "type",
            "type_class",
            "is_ending",
            "get_absolute_url",
        )
    
    def get_type_class(self,obj):
        return obj.get_type_display()

class ChoiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("text",)

class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("name", "prompt",)
