
from django.contrib import admin
from django.urls import path
from bursaryapp import views
app_name='bursaryapp'
urlpatterns = [
	path('dashboard',views.index,name='dashboard'),
	path('',views.index,name='index'),
	
]
