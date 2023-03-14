from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main-america'),
    path('index.html', views.main, name='main2-america'),
    path('brasil.html', views.brasil, name='brasil-america'),
    path('mexico.html',views.mexico, name='mexico-america'),
    path('argentina.html', views.argentina, name='argentina-america')
]