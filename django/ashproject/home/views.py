from django.shortcuts import render

# Create your views here.
#password for test user is harry@123
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')

