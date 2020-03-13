from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as doLogout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm
def index(request):

    if request.method == 'POST' and request.POST['type'] == 'register':
        form_register =SignUpForm(request.POST)
        if form_register.is_valid():
            form_register.save()
            username = form_register.cleaned_data.get('email')
            password = form_register.cleaned_data.get('password1')
            #user = authenticate(username=username,password=password)
            #login(request, user)
            return redirect('/')
    else:
        form_register = SignUpForm()

    if request.method == 'POST' and request.POST['type'] == 'login':
        form_login = AuthenticationForm(data=request.POST)
        if form_login.is_valid():
            user = form_login.get_user()
            login(request, user)
            return redirect('/wish')
    else:
        form_login = AuthenticationForm()
    context = {
        'form_login' : form_login,
        'form_register': form_register
    }
    return render(request, 'index.html', context)

def logout(request):
    doLogout(request)
    return  redirect('/')


