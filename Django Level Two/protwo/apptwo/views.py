from django.shortcuts import render
from django.http import HttpResponse
from apptwo.models import users

# Create your views here.

def index(request):
    my_dist={'insert_me':'Go to /user to see users_list'}
    return render(request,"apptwo/index.html", context=my_dist )
    # return HttpResponse("hi usman")

def user(request):
    user_list=users.objects.order_by('first_name')
    user_dict={'user_dict':user_list}
    return render(request,"apptwo/user.html",context=user_dict)