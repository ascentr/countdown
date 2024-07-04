from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect


def home(request):
  return render(request, 'home.html')
