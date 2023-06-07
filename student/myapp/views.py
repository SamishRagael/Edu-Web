from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"myapp/homepage.html")
def taketest(request):
    return render(request,"myapp/taketest.html")

