from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):  # django uses request object so we have to pass it to function index.
    my_dict={'insert_me': "Now i'm comming from firstapp/index.html!" }
    return render(request, 'firstapp/index.html',context=my_dict)

    # return HttpResponse("Hello world")
