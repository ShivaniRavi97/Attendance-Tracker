from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Subject,Sgpa,Cgpa



# Create your views here.
def signin(request):
	if request.user.is_authenticated:
		return redirect("/task/")

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect("/task/")
	return render(request,"login.html")



def signout(request):
	logout(request)
	return render(request,"login.html")


def signup(request):
	if request.method == "POST":
		username = request.POST.get('username',None)
		email = request.POST.get('email',None)
		password = request.POST.get('password',None)
		try:
			user = User.object.get(username=username)
			error ="User already exists."
			return render(request, "signup.html", {"error":error})
		except:
			user = User.objects.create_user(username, email,password)
			login(request,user)
			return redirect("/task/")
			
	return render(request,"signup.html")

def home(request):
	if request.user.is_authenticated:
		return redirect("/task/")
	return render(request, "home.html")

def attend(request):
	return render(request, "att.html")

def task(request):
	return render(request, "task1.html")

def add_subjects(request):
	if request.method == "POST":
		total =float(request.POST.get('total'))
		name = request.POST.get('name')
		user = request.user
		sub=Subject(total=total, name=name,user=user)
		sub.save()
		subs = Subject.objects.filter(user=user)
		return render(request, "add.html", {"subs":subs})

	return render(request, "add.html")

def update_attendance(request):
	subs= Subject.objects.filter(user=request.user)
	if request.method == "POST":
		subid=int(request.POST.get('subject'))
		sub=Subject.objects.get(pk=subid)
		total=sub.total
		absent= int(request.POST.get('absent'))
		sub.absent = absent
		att=((absent)/(total))*100
		att_perc=100-att
		sub.att_perc = att_perc
		sub.save()
		return render(request, "update.html", {"subs":subs,"absent":absent,"att_perc":att_perc})

	return render(request, "update.html",{"subs":subs})

def display_attendance(request):
	subs= Subject.objects.filter(user=request.user)
	return render(request, "display.html",{"subs":subs})

def sgpa(request):
	if request.method == "POST":
		credit1 = request.POST.get('credit1')
		grade_point1 = request.POST.get('grade_point1')
		credit_pt1=(int(credit1))*(int(grade_point1))
		credit2 = request.POST.get('credit2')
		grade_point2 = request.POST.get('grade_point2')
		credit_pt2=(int(credit2))*(int(grade_point2))
		credit3 = request.POST.get('credit3')
		grade_point3 = request.POST.get('grade_point3')
		credit_pt3=(int(credit3))*(int(grade_point3))
		credit4 = request.POST.get('credit4')
		grade_point4 = request.POST.get('grade_point4')
		credit_pt4=(int(credit4))*(int(grade_point4))
		credit5 = request.POST.get('credit5')
		grade_point5 = request.POST.get('grade_point5')
		credit_pt5=(int(credit5))*(int(grade_point5))
		credit6 = request.POST.get('credit6')
		grade_point6 = request.POST.get('grade_point6')
		credit_pt6=(int(credit6))*(int(grade_point6))
		credit7 = request.POST.get('credit7')
		grade_point7 = request.POST.get('grade_point7')
		credit_pt7=(int(credit7))*(int(grade_point7))
		credit8 = request.POST.get('credit8')
		grade_point8 = request.POST.get('grade_point8')
		credit_pt8=(int(credit8))*(int(grade_point8))
		tot_c=(int(credit1))+(int(credit2))+(int(credit3))+(int(credit4))+(int(credit5))+(int(credit6))+(int(credit7))+(int(credit8))
		tot_cp=(int(credit_pt1))+(int(credit_pt2))+(int(credit_pt3))+(int(credit_pt4))+(int(credit_pt5))+(int(credit_pt6))+(int(credit_pt7))+(int(credit_pt8))
		tot_sgpa=(float(tot_cp))/(float(tot_c))
		percent=float((tot_sgpa-0.75)*10)
		print(tot_c)
		print(tot_cp)
		return render(request, "sgpa.html",{"credit_pt1":credit_pt1,"credit_pt2":credit_pt2,"credit_pt3":credit_pt3,"credit_pt4":credit_pt4,"credit_pt5":credit_pt5,"credit_pt6":credit_pt6,"credit_pt7":credit_pt7,"credit_pt8":credit_pt8,"tot_sgpa":tot_sgpa,"percent":percent})

	return render(request, "sgpa.html")

def cgpa(request):
	if request.method == "POST":
		c1 = request.POST.get('c1')
		sg1 = request.POST.get('sg1')
		c2 = request.POST.get('c2')
		sg2 = request.POST.get('sg2')
		c3 = request.POST.get('c3')
		sg3 = request.POST.get('sg3')
		c4 = request.POST.get('c4')
		sg4 = request.POST.get('sg4')
		c5 = request.POST.get('c5')
		sg5 = request.POST.get('sg5')
		c6 = request.POST.get('c6')
		sg6 = request.POST.get('sg6')
		c7 = request.POST.get('c7')
		sg7 = request.POST.get('sg7')
		c8= request.POST.get('c8')
		sg8 = request.POST.get('sg8')
		total_cg=((float(c6))*(float(sg6))+(float(c5))*(float(sg5))+(float(c7))*(float(sg7))+(float(c8))*(float(sg8))+(float(c3))*(float(sg3))+(float(c2))*(float(sg2))+(float(c1))*(float(sg1))+(float(c4))*(float(sg4)))
		total_c=(float(c1))+(float(c2))+(float(c3))+(float(c4))+(float(c5))+(float(c6))+(float(c7))+(float(c8))
		total=(float(total_cg))/(float(total_c))
		percentage=float((total-0.75)*10)
		return render(request, "cgpa.html",{"total":total,"percentage":percentage})	
	
	return render(request, "cgpa.html")