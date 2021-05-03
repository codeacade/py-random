from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainView),     ## this is main Ajax website
    path('calc', views.mainCalc), ## this will only calculate response for Ajax

]
