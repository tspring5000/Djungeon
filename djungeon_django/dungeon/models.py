import uuid
import random
from django.db import models
from django.urls import reverse

class Choice(models.Model):
    text = models.CharField(max_length=25)
    room = models.ForeignKey(
        to='Room',
        on_delete=models.CASCADE,
        related_name="linked_choices",
    )


class RoomManager(models.Manager):
    def generate(self, **obj_data):
        all_rooms = Room.objects.all()
        room1 = random.choice(list(all_rooms))
        room2 = random.choice(list(all_rooms.exclude(pk=room1.pk)))

        choice1 = Choice.objects.create(
            text = obj_data["choice_1_text"],
            room = room1
        )
        choice2 = Choice.objects.create(
            text = obj_data["choice_2_text"],
            room = room2
        )

        new_room = self.create(
            name = obj_data["name"],
            prompt = obj_data["prompt"],
            choice_1 = choice1,
            choice_2 = choice2,
        )

        return new_room

ROOM_TYPES = [
    (0, "normal"),
    (1, "win-ending"),
    (2, "lose-ending"),
]

class Room(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    name = models.CharField(max_length=25)
    prompt = models.CharField(max_length=250)

    # The related_names will go unused as a Choice will only ever be either Choice1 or Choice2
    # However Django will complain about clashes without the related_names
    choice_1 = models.OneToOneField(
        Choice,
        related_name="room_choice1",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    choice_2 = models.OneToOneField(
        Choice,
        related_name="room_choice2",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    type = models.IntegerField(
        choices=ROOM_TYPES,
        default=0
    )

    objects = RoomManager()

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("room-detail", kwargs={"room_uuid": self.uuid})
    
    @property
    def is_ending(self):
        return self.type > 0
