from django.shortcuts import render
from django.http import HttpResponse
from firstapp.forms import UserForm,UserProfileInfoForm

#

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):  # django uses request object so we have to pass it to function index.
    context_dict={'text':'hello world','number':100}
    return render(request, 'firstapp/index.html',context_dict)

@login_required
def special(request):
    return HttpResponse("You are login, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    # assume user is not registered
    registered = False
    
    if request.method == 'POST':
        # get data from both forms
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        
        # check if both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # save user's form data to database
            user = user_form.save()
            user.set_password(user.password) # hash the password
            user.save()

            # save profile form data to database
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            # registration was successful
            registered = True
        else:
            # print errors to console
            print(user_form.errors, profile_form.errors)
    else:
        # display empty forms for GET requests
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'firstapp/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })


def user_login(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account NOT Active")
        
        else:
            print("Some one tried to login and failed")
            print("username {} and password {}".format(username,password))

            return HttpResponse("Invalid login details")
        
    else:
        return render(request,'firstapp/login.html',{})