from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.


def index(request):  # django uses request object so we have to pass it to function index.

    return render(request, 'firstapp/index.html')

def form_name_view(request):
    form = forms.FormName

    if request.method =='POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success full")
            print("Name :"+ form.cleaned_data["name"])
            print("Email :"+ form.cleaned_data["email"])
            print("Text :"+ form.cleaned_data["text"])
            
            
    return render(request, 'firstapp/form_page.html', {'form': form})

