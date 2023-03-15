from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic, AccessRecord, Webpage 
# Create your views here.

def index(request):  # django uses request object so we have to pass it to function index.
    # my_dict={'insert_me': "Now i'm comming from firstapp/index.html!" }
    Webpagelist=AccessRecord.objects.order_by("date")
    date_dict={'acc_rec':Webpagelist}
    return render(request, 'firstapp/index.html',context=date_dict)

    # return HttpResponse("Hello world")

