from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('google_earth/', views.google_earth, name='google_earth'),
]
