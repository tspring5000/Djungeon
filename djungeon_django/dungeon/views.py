from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, DetailView
from .models import Room
from .forms import RoomCreateForm


class RoomCreateView(CreateView):
    template_name = "dungeon/room_create.html"
    form_class = RoomCreateForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        data = form.cleaned_data
        new_room = Room.objects.generate(
            name=data["name"],
            prompt=data["prompt"],
            choice_1_text=data["choice_1_text"],
            choice_2_text=data["choice_2_text"]
        )
        return HttpResponseRedirect(self.get_success_url(new_room))

    def get_success_url(self, room):
        return room.get_absolute_url()


class RoomDetailView(DetailView):
    template_name = "dungeon/room_detail.html"
    queryset = Room.objects.all()

    def get_object(self):
        return Room.objects.get(uuid=self.kwargs["room_uuid"])
