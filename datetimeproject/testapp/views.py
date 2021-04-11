from django.shortcuts import render
import datetime

# Create your views here.
def time(request):
    time=datetime.datetime.now()
    my_dict={'date':time}
    return render(request,'testapp/time.html',context=my_dict)
