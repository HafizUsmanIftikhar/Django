from django.shortcuts import render
# from django.http import HttpResponse
# from apptwo.models import users

from apptwo.form import NewUserForm


# Create your views here.

def index(request):
    my_dist={'insert_me':'Go to /user to SignUp! '}
    return render(request,"apptwo/index.html", context=my_dist )

def user(request):
    form=NewUserForm()

    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            return index(request)
    
    return render(request,"apptwo/user.html",{'form':form})

    