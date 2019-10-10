from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from .models import *
from .forms import *
import datetime


def Add(request):
    print("IN ADD")
    form=DiaryForm()
    if request.method=='POST':
        form=DiaryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
    return render(request,'form.html',{'form':form})

def Delete(request):
    print("IN DELETE")
    o=Diary.objects.all()
    if request.POST.get('Delete'):
        for i in o:
            try:
                obj=str(i.date_time)
                is_private=request.POST[obj]
            except MultiValueDictKeyError:
                pass
            else:
                i.delete()

    else:
        o=Diary.objects.all()
        for i in o:
            try:
                obj=str(i.date_time)
                is_private = request.POST.get(obj)
            except MultiValueDictKeyError:
                is_private = False
        i.delete()
    return redirect('home')

def Update(request,date):
    print("IN UPDATE")
    o=Diary.objects.get(date_time=date)
    print("#------->",o)
    text=o.text
    o.delete()
    form=DiaryForm(initial={'text': text})
    return render(request,'form.html',{'form':form})

def Home(request):
    print("IN HOME")
    o=Diary.objects.order_by('date_time')
    if o:
        o=o.reverse()
    return render(request,'home.html',{'obj':o,'val':datetime.date.today()})
