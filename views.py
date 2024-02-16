from django.shortcuts import render , redirect
from django.http import HttpResponse

from test_project import settings
from .models import memberdetails
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.

def home(request):
    #print(request.user)
    
    return render(request,"Home.html")

   
def User_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']       
        member = authenticate(request,username=username,password=password)
        
        if member:
            login(request,member)
            messages.success(request,'')
            return redirect('landing')
        else:
            messages.warning(request,'')
       
         

    return render(request,"login.html")

def Logout(request):
    print('hiii')
    logout(request)
    return redirect("login/")



def reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if memberdetails.objects.filter(email=email).first():
            context = {'user_name': 'joanreshmi@gmail.com',
                    'password_link': 'http://127.0.0.1:8000/reset_confirm',
                    'content': "this link for use for password reset",
                    }
            subject='password reset'
            from_email=str(settings.EMAIL_HOST_USER)
            recipient_list =[email]
            html_message = render_to_string('notification.html', context)
            plain_message = strip_tags(html_message)

            mail.send_mail(subject=subject, message=plain_message, from_email=from_email, recipient_list=recipient_list, html_message=html_message)
            return redirect(Resetdone)
    return render(request,"reset.html")

def Resetdone(request):
    return render(request,"reset_done.html")


def Resetconfirm(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['psw']
        confirm_password=request.POST['confirm_password']
        #print("asdfghjkl;")
        member_detail = memberdetails.objects.filter(email=email,is_active=True).first()
        print(member_detail,"member")
        if member_detail:
            if password == confirm_password:
                # print(password)
                # print(confirm_password)
                hashed_password = make_password(password)
                member_detail.password=hashed_password
                member_detail.save()
                # print("saved")
                return redirect(home)
               
            else:
                messages.warning(request,'Please Provide Same Confirm Password')
        else:
            messages.warning(request,'member not exist')
        
    return render(request,"reset_confirm.html")

def Resetcomplete(request):
    return render(request,"reset_complete.html")

    

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['psw']
        confirm_password=request.POST['confirm_password']
        profile_pic=request.FILES['image']
        
        if password != confirm_password:
            messages.warning(request,'Please Provide Same Confirm Password')
            return render(request,'register.html')
        
        if memberdetails.objects.filter(email=email).first():
            messages.warning(request,'Email Already Exist')
            return render(request,'register.html')
        
        
        obj = memberdetails()
        obj.username=username
        obj.email=email
        obj.set_password(password)
        obj.profile_pic=profile_pic
        obj.save()     
        
        return redirect('user_login')
    return render(request,"register.html")

def landing(request):
    
        mydata=memberdetails.objects.all()
        print(mydata)
        return render(request,"landing.html",{"member":mydata})
     
def Update(request,id):
    mydata=memberdetails.objects.get(id=id)
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        profile_pic=request.FILES['image']
        
       
        
      
             
        # mydate = memberdetails()
        mydata.username=username
        mydata.email=email
        mydata.profile_pic=profile_pic
        mydata.save()

        return redirect(landing)
    
    return render(request,'update.html',{'member':mydata})

def Delete(request,id):
        mydata=memberdetails.objects.get(id=id)
        mydata.delete()
        return redirect(landing)



       
  

    
 


