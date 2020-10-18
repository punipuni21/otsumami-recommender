from django.urls import path

from . import views

urlpatterns = [
    path('', views.estimate, name='estimate'),
    path('image/', views.showimage, name='image'),
]