from django.shortcuts import render
from django.views.generic import TemplateView
import datetime

# Create your views here.

class AlarmClockClass(TemplateView):
    template_name = 'alarmclock.html'