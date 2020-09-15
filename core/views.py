from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import datetime as dt
from .forms import Visitors, Meetings
from .models import ntpcusers,ntpcvisitors

#############################################################################################
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

def meetings(request):
    context = {
        'meetings':ntpcvisitors.objects.filter(timein__date = dt.date.today())
    }
    return render(request, 'meetings.html', context )

def meetings_add(request):
    if request.method == 'POST':
        form = Meetings(request.POST)
        meeting_added = form.save()
        form = Meetings(initial={'timein':datetime.now, 'timeout':datetime.now})
        context = {'form':form, 'added':meeting_added  }
        return render(request, 'meetings_add.html', context )
    else:
        form = Meetings(initial={'timein':datetime.now, 'timeout':datetime.now})
        context = {'form':form }
        return render(request, 'meetings_add.html', context )
