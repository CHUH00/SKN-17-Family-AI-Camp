from django.urls import path
from second import views

app_name = 'second'

urlpatterns = [
    path('', views.index, name='index'),
]