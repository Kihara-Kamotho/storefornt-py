# in this file we match our url to view fncs, hence the name 
from django.urls import path 
from . import views 

# urlconfig
urlpatterns = [
  path('hello/', views.say_hello),
  path('welcome/', views.say_welcome)
]