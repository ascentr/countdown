from django.shortcuts import render , redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import SignupForm

def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)

      if 'next' in request.POST:
        return redirect(request.POST.get('next'))
      else:
        return redirect('index')
    else:
      return redirect('registration:signup')
  else:
    form = SignupForm()
  
  return render(request, 'registration/signup.html', {'form': form})
  