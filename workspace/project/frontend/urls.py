from django.urls import path
from . import views

app_name="frontend"
urlpatterns = [
    path('', views.index, name="index" ),
    path('submit', views.submit, name="submit"),
    path('quiz', views.quiz, name="quiz"),
    path('photo', views.photo, name="photo"),
    path('result', views.result, name="result")

]
