from django.shortcuts import render,HttpResponseRedirect
from .forms import Student
from .models import Data
# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = Student(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Student()
             
    else:
        fm = Student()
    form = Data.objects.all() 
    return render(request,'enroll/home.html',{'forms':fm,'form':form})

def delete(request, id):
    if request.method == 'POST':
        pi = Data.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request, id):
    if request.method == 'POST':
        pi = Data.objects.get(pk=id)
        fm = Student(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Data.objects.get(pk=id)
    fm = Student(instance=pi)
    return render(request,'enroll/update.html',{'forms':fm})