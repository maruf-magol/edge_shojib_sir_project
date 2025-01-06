from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.
def home(request):
    print("HOME")
    return render(request,"home.html")

def about(request):
    if request.method == 'POST':
        new_name = request.POST.get('name_input')
        new_roll = request.POST.get('roll_input')
        new_user = User(name=new_name,roll=new_roll)
        new_user.save()
        contexts = {
            "new_user": new_user,
        }
        return render(request,"about.html",contexts)
    else:
        print("GET")
        return render(request,"about.html")

def contact(request):
    all_user = User.objects.all()
    contexts = {
        "all_user":all_user
    }
    return render(request,"contact.html",context=contexts)

def posts(request):
    context = {
    }
    return render(request,"posts.html",context=context)
