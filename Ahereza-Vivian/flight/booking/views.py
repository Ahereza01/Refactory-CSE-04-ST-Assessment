from django.shortcuts import render, redirect
from .models import Passenger
from .forms import BookingForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = BookingForm()    
    
    return render(request,'index.html',{'form':form})

# Create your views here.
