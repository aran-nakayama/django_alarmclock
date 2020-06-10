from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
import datetime
from .models import TimeModel
from django.urls import reverse_lazy

# Create your views here.

class AlarmClockClass(UpdateView):
    template_name = 'alarmclock.html'
    model = TimeModel
    fields = ('hour', 'minute')
    success_url = reverse_lazy('waiting')

class WaitingPage(ListView):
    template_name = 'waiting.html' 
    model = TimeModel

class SoundPage(TemplateView):
    template_name = 'sound.html'