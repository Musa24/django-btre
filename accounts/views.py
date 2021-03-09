from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth



def register(request):
    if request.method == "POST":
        # messages.error(request,"Testing error message")
        # return redirect("register")
        # GET FORM VALUES
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
      
        # Check password(match)
        if password == password2:
            #check username (unique)
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username is already exits")
                return redirect("register")
            else:
                # check email(unique)
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email is already registered")
                    return redirect("register")
                else:
                    # Create user 
                    user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                    # login after register
                    # auth.login(user)
                    user.save()
                    messages.success(request,"You are now registered")
                    return redirect("login")
        else:
            messages.error(request,"Password do not match")
            return redirect("register")
    else:
        return render(request, "accounts/register.html")

def login(request):
    
    return render(request, "accounts/login.html")

def logout(request):
    pass


def dashboard(request):
    return render(request, "accounts/dashboard.html")