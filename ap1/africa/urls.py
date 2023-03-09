from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main-africa'),
    path('angola.html',views.angola, name='angola-africa'),
    path('magascar.html',views.madagascar, name='madagascar-africa')
]