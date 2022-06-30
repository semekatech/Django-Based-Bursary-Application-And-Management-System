
from django.contrib import admin
from django.urls import path
from accounts import views
app_name='accounts'
urlpatterns = [
	path('register',views.registration_view,name='register'),
	path('login/',views.login_view, name='login'),
]
