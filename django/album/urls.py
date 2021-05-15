from django.urls import path
from . import views

urlpatterns = [
  path('', views.galleryView, name="gallery"),
  path('image/<str:pk>', views.imageView, name="image"),
  path('add', views.addImageView, name="add"),

]
