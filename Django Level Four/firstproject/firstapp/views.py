from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):  # django uses request object so we have to pass it to function index.
    context_dict={'text':'hello world','number':100}
    return render(request, 'firstapp/index.html',context_dict)

def base(request):
    return render(request, 'firstapp/base.html')


def other(request):
    return render(request, 'firstapp/other.html')

def relative(request):
    return render(request, 'firstapp/relative_url_template.html')

