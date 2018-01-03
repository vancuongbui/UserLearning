from django.shortcuts import render
from userApp.forms import UserForm, UserProfileInfoForm

#for using login/logout from import
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'userApp/index.html')

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("Your are logged in now")


def register(request):
    registered = False

    if request.method == "POST":
        userForm = UserForm(data=request.POST)
        profileForm = UserProfileInfoForm(data=request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user

            if 'profilePics' in request.FILES:
                profile.profilePics = request.FILES('profilePics')

            profile.save()
            registered = True
        else:
            print(userForm.errors, profileForm.errors)
    else:
        userForm = UserForm()
        profileForm = UserProfileInfoForm()

    return render(request,'userApp/register.html',
                    {'userForm':userForm,
                    'profileForm':profileForm,
                    'registered':registered})

def userLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}").format(username, password)
            return HttpResponse("Invalid username and/or password")
    else:
        return render(request, 'userApp/login.html',{})
