import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.forms import RegisterForm, LoginForm, Verifyform, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user.models import Profile, EMAILCodes
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
                last_name=last_name,
                is_active=False
            )
            Profile.objects.create(
                user=user,
                avatar=avatar,
                bio=bio,
            )
            code = ''.join([str(random.randint(0, 9)) for _ in range(5)])
            EMAILCodes.objects.create(
                user=user,
                code=code
            )

            return redirect('verify')
        else:
            return render(request, 'user/register.html', {'form': form})

def verify_view(request):
    if request.method == 'GET':
        return render(request, 'user/verify.html', {'form': Verifyform()})
    elif request.method == 'POST':
        form = Verifyform(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if EMAILCodes.objects.filter(code=code).exists():
                email_code = EMAILCodes.objects.get(code=code)
                email_code.user.is_active = True
                email_code.save()
                email_code.delete()
                return redirect('login')
            else:
                form.add_error(None, 'Code does not exist')
                return render(request, 'user/verify.html', {'form': form})



def login_view(request):
    if request.method == 'GET':
        return render(request, 'user/login.html', {'form': LoginForm()})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
           user = authenticate(**form.cleaned_data)
           
           if user is not None:
               login(request, user)
               return redirect('products_list')
           else:
               form.add_error(None, 'Invalid credentials')
               return render(request, 'user/login.html', {'form': form})

def profile_view(request):
    return render(request, 'user/profile.html')

@login_required
def profile_update_view(request):
    if request.method == 'GET':
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(
            initial={
                'username': request.user.username,
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'avatar': profile.avatar,
                'bio': profile.bio,
            }
        )

        return render(request, 'user/profile_update.html', {'form': form})
    elif request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.username = form.cleaned_data['username']
            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.save()

            profile = Profile.objects.get(user=request.user)
            profile.avatar = form.cleaned_data['avatar']
            profile.bio = form.cleaned_data['bio']
            profile.save()

            return redirect('profile')
        else:
            return render(request, 'user/profile_update.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('products_list')