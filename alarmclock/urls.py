from django.urls import path
from .views import AlarmClockClass, WaitingPage

urlpatterns = [
    path('alarmclock/', AlarmClockClass.as_view(), name = 'alarmclock'),
    path('waiting/', WaitingPage.as_view(), name='waiting'),
]