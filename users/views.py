import json

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login(request):
    return render(request, 'users/login.html')


def registration(request):
    users = {
        'username': request.user.username,
    }
    return HttpResponse(json.dumps(users)) # render(request, 'users/register.html')
