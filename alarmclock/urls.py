from django.urls import path
from .views import AlarmClockClass

urlpatterns = [
    path('alarmclock/', AlarmClockClass.as_view()),
]