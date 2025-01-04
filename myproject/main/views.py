from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    print("HOME")
    return render(request,"home.html")

def about(request):
    if request.method == 'POST':
        temp = int(request.POST.get('name_input'))
        contexts = {
            "NAME": [i+1 for i in range(temp)],
        }
        return render(request,"about.html",contexts)
    else:
        print("GET")
        return render(request,"about.html")

def contact(request):
    
    return render(request,"contact.html")

def posts(request):
    
    return render(request,"posts.html")
