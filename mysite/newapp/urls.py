from . import views
from django.urls import path

app_name = 'newapp'

urlpatterns = [
    path('', views.index, name='index')
]