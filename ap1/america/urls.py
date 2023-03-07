from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main-america'),
    path('brasil.html', views.brasil,name='brasil-america'),
]