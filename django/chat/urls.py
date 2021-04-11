## REDIRECTED FROM proj/urls.py with
## path('chat/', include('chat.urls')),

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),        # main page
    path('log', views.log_in),    # custom user login page
    path('alert', views.alert),   # test alert page

]
