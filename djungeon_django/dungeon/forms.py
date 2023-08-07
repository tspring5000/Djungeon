from django import forms
from .models import Room


def input_attributes(placeholder, rows=1):
    return {
        "class": "shadow-box",
        "placeholder": placeholder,
        "cols": 25,
        "rows": rows,
    }


class RoomCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=25,
        widget=forms.Textarea(
            attrs=input_attributes("The Corridor of Choice")
        )
    )

    prompt = forms.CharField(
        max_length=250,
        widget=forms.Textarea(
            attrs=input_attributes(
                "You find yourself at a junction, do you...", 10
            )
        )
    )

    choice_1_text = forms.CharField(
        max_length=25,
        widget=forms.Textarea(
            attrs=input_attributes("Turn left")
        )
    )

    choice_2_text = forms.CharField(
        max_length=25,
        widget=forms.Textarea(
            attrs=input_attributes("Turn right")
        )
    )

    class Meta:
        model = Room
        fields = [
            "name",
            "prompt",
            "choice_1_text",
            "choice_2_text"
        ]
