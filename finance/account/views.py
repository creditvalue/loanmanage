from account.models import Uhistory, loanapply
from django.core.checks import messages
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.db import transaction
from django.contrib import messages
from .forms import ImageForm
# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == 'POST': 
        mobile = request.POST['mobile']
        if User.objects.filter(mobile = mobile).first():
            messages.error(request, "This Mobile is already taken")
            return HttpResponseRedirect('/register') 
        else:    
            fname = request.POST['fname']
            lname = request.POST['lname']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if pass1 == pass2:
                myuser = User.objects.create_user(mobile, pass1)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()
                return render(request,"done.html")
            else:
                messages.success(request, 'password and confirm pass not match')
                return HttpResponseRedirect('/register')   
    return render(request,"register.html")    

def userlogin(request):
    if request.method == "POST":
        mobile = request.POST['mobile']
        password = request.POST['password']
        user = authenticate(request, mobile=mobile, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/u_profile/') 
        else:
            messages.warning(request, 'Incorrect mobile and password')
            return HttpResponseRedirect('/userlogin/')       
    else:
        return render(request,"login.html")    

def u_profile(request):
    user = User.objects.all()
    usera = User.objects.get(id = request.user.id)
    history = Uhistory.objects.filter(user=usera)
    parms = {'User':user,'Uhistory':history}
    return render(request,"u-profile.html",parms)         

def userlogout(request):
        logout(request)
        return HttpResponseRedirect('/userlogin/')  

def addmoney(request):
    if request.method == "POST":
        messages.success(request, 'Your money add in wallet')
        return HttpResponseRedirect('/u_profile/')
    else:
        return render(request,"inceasu.html")

def sendmon(request):
    if request.method == "POST":
        try:
            user = User.objects.get(id = request.user.id)
            addbal = request.POST.get('money')
            addbal = int(addbal)
            with transaction.atomic():
                if user.balance > addbal:
                    finduser = request.POST.get('mobile')
                    user.balance -= addbal
                    user.save()
                    # update user history
                    hist = Uhistory(user=user,dmoney = addbal,histype="Send To",ufrom=finduser)
                    hist.save()
                    # add money to another user 
                    finduser = request.POST.get('mobile')
                    userb = User.objects.get(mobile = finduser)
                    userb.balance += addbal
                    userb.save()
                    # finduser user history update
                    fromuser = user.mobile
                    hist = Uhistory(user=userb,dmoney = addbal,histype="Recieved By",ufrom = fromuser)
                    hist.save()
                    return render(request,"paysuccess.html")
                else:
                    messages.success(request, 'Your low money')
                    return HttpResponseRedirect('/sendmon/')
        except Exception as e:
            print(e)
            messages.warning(request, 'User not find')
            return HttpResponseRedirect('/sendmon/')         
    else:
        return render(request,"sendbal.html")

def history(request):
    user = User.objects.get(id = request.user.id)
    history = Uhistory.objects.filter(user=user)
    return render(request,"hist.html",{'Uhistory':history}) 

def checkpoint(request):

    return render(request,"done.html")  

def applyloan(request):
    if request.method == "POST":
        user = User.objects.get(id = request.user.id)
        loanam = request.POST.get('loana')
        loantype = request.POST.get('allloans')
        lonamo = user.mobile
        loanfn= user.first_name
        loanapp = loanapply(name=loanfn,lmobile=lonamo,amount=loanam,tloan=loantype)
        loanapp.save()
        return render(request,"paysuccess.html")
    else:
        return render(request,"apploan.html")     