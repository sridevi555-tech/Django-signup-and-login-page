from django.shortcuts import render

#create your views here
def HomePage(request):
    pass
def SignupPage(request):
    return render(request,'signup.html')
def LoginPage(request):
    return render(request,'login.html')