from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def homepage(request):

    return HttpResponse('hi <a href="/user/logout/">logout</a>')

def logout(request):

    return HttpResponseRedirect('/user/login/')