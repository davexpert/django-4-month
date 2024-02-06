from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from user.models import Profile
def register_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html', {'form': RegisterForm()})
    elif request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            avatar = form.cleaned_data['avatar']
            bio = form.cleaned_data['bio']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            Profile.objects.create(
                user=user,
                avatar=avatar,
                bio=bio,
            )

            return redirect('products_list')
        else:
            return render(request, 'user/register.html', {'form': form})

def login_view(request):
    if request.method == 'GET':
        return render(request, 'user/login.html', {'form': LoginForm()})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
           user = authenticate(**form.cleaned_data)
           
           if user:
               login(request, user)
               return redirect('products_list')
           else:
               form.add_error(None, 'Invalid credentials')
               return render(request, 'user/login.html', {'form': form})

def profile_view(request):
    return render(request, 'user/profile.html')

def logout_view(request):
    logout(request)
    return redirect('products_list')