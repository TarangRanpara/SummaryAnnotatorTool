from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import LogInForm, User, UserRegisterationForm
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

LOGIN_SUCCESS_REDIRECT = "/articles"

def make_session_entry(request, key, value):
    request.session[key] = value

def login_process(request, key, user_obj):
    print('session set.')
    make_session_entry(request, key, user_obj.get_username())
    login(request, user_obj)

def login_view(request):
    form = LogInForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if user != None:
            #login(request, user)
            #request.session['username'] = user.get_username()
            login_process(request, 'username', user)
            return redirect(LOGIN_SUCCESS_REDIRECT)
        else:
            # attempt = request.session.get('attempt') or 0
            # request.session['attempt'] = attempt + 1
            request.session["invalid_user"] = 1
    
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("/login")

def register_view(request):
    form = UserRegisterationForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        try:
            user = User(email = email, username= username, password =make_password(password1))
            user.save()
        except Exception as e:
            user = None 
            print(e)
        if user != None:
            #login(request, user)
            #request.session['username'] = user.get_username()
            login_process(request, 'username', user)
            return redirect(LOGIN_SUCCESS_REDIRECT)
        else:
            request.session["registration_error"] = 1
    return render(request, "register.html", {"form": form})