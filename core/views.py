from django.shortcuts import render
from django.http import HttpResponse
from .forms import Visitors
from .models import ntpcusers

def visitors(request):
    context = {
        'noOfNTPCVisitors':ntpcusers.objects.count()
    }
    return render(request, 'visitors.html', context )

def visitors_add(request):
    if request.method == 'POST':
        form = Visitors(request.POST)
        useradded = form.save()
        form = Visitors()
        context = {'form':form, 'added':useradded }
        return render(request, 'visitors_add.html', context )
    else:
        form = Visitors()
        context = {'form':form }
        return render(request, 'visitors_add.html', context )

def visitors_list(request):
    context = {'NTPCUserList':ntpcusers.objects.all()}
    return render(request, 'visitors_list.html', context )

def visitors_edit(request,int):
    context = {'NTPCUserList':ntpcusers.objects.all()}
    return render(request, 'visitors_list.html', context )