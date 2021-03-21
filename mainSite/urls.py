from django.urls import path, include
from . import views

app_name = 'mainSite'
urlpatterns = [
    path('',views.Home.as_view(), name='app-home'),
    path('footballmanager', views.Football.as_view(), name='app-football')
]