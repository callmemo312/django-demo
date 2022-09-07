from django.urls import path
from device_manage.views import IndexView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index')
]