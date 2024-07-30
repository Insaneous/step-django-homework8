from django.urls import path
from postapp import views


urlpatterns = [
    path('', views.index, name='index'),
]