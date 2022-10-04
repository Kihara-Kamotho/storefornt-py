from django.shortcuts import render

# Create your views here.
# here we add actions that point to view templates 
# these views can also be refered to as request handlers/action 
from django.shortcuts import render 
from django.http import HttpResponse 

def say_hello(request):
  # return HttpResponse('Hello World') 
  return render(request, 'hello.html', {'name': 'Py'})

# once we write the action we then match it to a url, to render it as a template 

def say_welcome(request):
  return HttpResponse('Welcome to django') 