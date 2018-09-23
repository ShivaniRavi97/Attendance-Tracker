from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from .models import Subname


# Create your views here.
def signin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			HttpResponse("logged in successfully")
	return render(request,"login.html")



def signout(request):
	logout(request)
	return render(request,"login.html")


def signup(request):
	if request.method == "POST":
		username = request.POST.get('username',None)
		email = request.POST.get('email',None)
		password = request.POST.get('password',None)
		user = authenticate(request, username=username, password=password)
		if user is None:
			user = User.objects.create_user(username, email,password)
			return HttpResponse("successfull created an account")
		else:
			return HttpResponse("user already exists")
	return render(request,"signup.html")

def subs(request):
	if request.method == "POST":
		max_length=request.POST.get('max_length=20')
		sub1 = request.POST.get('sub1')
		sub2 = request.POST.get('sub2')
		sub3 = request.POST.get('sub3')
		sub4 = request.POST.get('sub4')
		sub5 = request.POST.get('sub5')
		sub6 = request.POST.get('sub6')
		tot1 = request.POST.get('tot1')
		tot2 = request.POST.get('tot2')
		tot3 = request.POST.get('tot3')
		tot4 = request.POST.get('tot4')
		tot5 = request.POST.get('tot5')
		tot6 = request.POST.get('tot6')
		att = request.POST.get('att')
		# n1=int((att/100)*tot1)
		print(sub1,tot1,sub2,tot2,sub3)
		return render(request,"subjects.html",{"sub1":sub1})

def cal(request,sub1_id):
	return render(request,"calender.html")
