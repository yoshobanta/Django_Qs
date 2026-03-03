from django.shortcuts import render
from app.forms import *

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def registration(request):
    EUMFO = UserMF()
    EPMFO = ProfileMF()
    d = {'EUMFO':EUMFO , 'EPMFO': EPMFO}
    
    if request.method == 'POST' and request.FILES :
        NMUMFDO = UserMF(request.POST)               #non modifiable user mf data obj . also we are only getting data so only req.post
        NMPMFDO = ProfileMF(request.POST,request.FILES)
        
        if NMUMFDO.is_valid() and NMPMFDO.is_valid():
            MUMFDO = NMUMFDO.save(commit=False)       # We convert it to modifiable .
            pw = NMUMFDO.cleaned_data['password']
            MUMFDO.set_password(pw)                 # set_pw is a method of user . used for one way encryption .
            MUMFDO.save()
            
            MPMFDO=NMPMFDO.save(commit=False)
            MPMFDO.username = MUMFDO
            MPMFDO.save()
        
    
    return render(request,'registration.html',d)



def home(request):
    if request.session.get('username'):
        username = request.session.get('username')
        d = {'username' : username}
        return render(request,'home.html',d)
        
    return render(request,'home.html')


def user_login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        AUO = authenticate(username = username , password = password)   # authenticate user obj (var = value , var = value)
        if AUO :
            if AUO.is_active :    # this is not a method
                login(request,AUO)
                request.session['username'] = username            #req.sess is a dict and we are creating a key:value pair
                return HttpResponseRedirect(reverse('home'))
            else :
                return HttpResponse('User is not active')
        else :
            return HttpResponse('Invalid user / User not registered')
        
                
    
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def profile_display(request):
    username = request.session.get('username')
    UO = User.objects.get(username = username)
    PO = Profile.objects.get(username = UO)
    
    d = {'UO' : UO , 'PO' : PO}
    
    return render(request,'profile_display.html',d)


@login_required
def change_password(request):
    if request.method == 'POST' :
        cp = request.POST['cp']
        un = request.session.get('username')             #username
        uo = User.objects.get(username = un)
        uo.set_password(cp)
        uo.save()
        return HttpResponse("Password is changed")
    return render(request,'change_password.html')



def forget_password(request):
    if request.method == 'POST' :
        username = request.POST['un']
        newpassword = request.POST['forgetpw']
        uo = User.objects.filter(username = username)[0]
        if uo :
            uo.set_password(newpassword)
            uo.save()
            return HttpResponse('Password is updated')
        else :
            return HttpResponse('Invalid User')
            
            
    
    return render(request,'forget_password.html')