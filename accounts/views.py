from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import auth,messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return  redirect('index')
        else:
            messages.error(request, 'Invalid user name')
            return redirect('login')
    else:
        return render(request,'login.htm')
        
        
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request,'Your Successfully logged out')
        return redirect('login')
    else:
        return redirect('login')

    

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            messages.error(request, 'user name is Password was not matching')
            redirect('register')
        else:
            if  CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'user name is already exists')
                redirect('register')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request,'Email is already registered')
                    return redirect('register')
                else:
                    user = CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                        email=email, phone=phone, address=address, password=password)
                    user.save()
                    user = CustomUser.objects.get(email=email)
                    if 'photo' in request.FILES: 
                        photo = request.FILES['photo']
                        user.photo =  photo #path_and_rename(username ,photo)

                    user.save()
                    messages.success(request,'Your Successfully registeres here')
                    return redirect('login')
        
    
    return render(request, 'register.htm')
