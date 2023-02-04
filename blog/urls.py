from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeView,name='home'),
    path('detail/<int:id>',views.detailView,name='detail')
]