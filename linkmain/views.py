# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from linkmain.models import link
from linkmain.forms import linkForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime 

def index(request):
    linklist = link.objects.all().order_by('-pub_date')[:5]
    return render_to_response('linkmain/index.html', {'linklist': linklist,
                                                      'user': request.user})

@login_required(login_url='/links/login')
def add(request):
    if request.method == 'POST':
        form = linkForm(request.POST) 
        if form.is_valid():
            newlink=form.save(commit=False)
            newlink.pub_date= datetime.now()
            newlink.save()
            
            return HttpResponseRedirect('/') 
    else:
        form = linkForm()

    return render_to_response('linkmain/add.html', {'form': form,
                                                    'action': '/links/add/',
                                                    'user': request.user},
                              context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            data=form.cleaned_data
            user = User.objects.create_user(data['username'],
                                            data['email'],
                                            data['password'])
            user.save()
            user=authenticate(username=data['username'], password=data['password']) 
            login(request, user)
            return HttpResponseRedirect('/') 
    else:
        form = RegisterForm()
    return render_to_response('linkmain/add.html', {'form': form,
                                                    'action': '/register/',
                                                    'user': request.user},
                              context_instance=RequestContext(request))
