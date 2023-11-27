

from django import forms
from django.utils import timezone

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline", "")
        if deadline:
            deadline_utc = timezone.localtime(deadline).astimezone(timezone.utc)

            now = timezone.now()
            if deadline_utc <= now + timezone.timedelta(hours=1):
                raise forms.ValidationError(
                    f"The deadline should be in an hour from the current time"
                    f"({now.strftime('%d.%m.%Y %H:%M %Z')}) or more."
                )
        return deadline


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
