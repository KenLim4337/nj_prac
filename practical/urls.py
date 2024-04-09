from django.urls import path
from . import views

app_name= 'practical' 


urlpatterns = [
    path('', views.home, name='home'),
]