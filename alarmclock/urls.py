from django.urls import path
from .views import AlarmClockClass, WaitingPage, SoundPage

urlpatterns = [
    path('alarmclock/<int:pk>', AlarmClockClass.as_view(), name = 'alarmclock'),
    #alarmclock/15 で更新できる。
    path('waiting/', WaitingPage.as_view(), name='waiting'),
    path('sound/', SoundPage.as_view(), name= 'sound'),
]