from django.shortcuts import render
from .models import Event
from django.utils import timezone
# Create your views here.


def events(request):
    events = Event.objects.filter(time__gt=timezone.now())
    context = {'events': events}
    return render(request, 'events/events.html', context)
