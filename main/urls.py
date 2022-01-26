from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='home'),
    path('multistepformexample', views.multistepformexample, name='multistepformexample'),
    path('multistepformexample_save', views.multistepformexample_save, name='multistepformexample_save'),
]