from django.shortcuts import render,redirect
from core.forms import UserForm
from .models import UserModel
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
	fm = UserForm()
	data = UserModel.objects.all()
	return render(request, "index.html",{'form':fm,'data':data})

def save_data(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			sid = request.POST.get("sid")
			name = request.POST['name']
			mobile = request.POST['mobile']
			password = request.POST['password']
			if sid == "":
				usr = UserModel(name=name,mobile=mobile,password=password)
			else:
				usr = UserModel(id=sid,name=name,mobile=mobile,password=password)

			usr.save()
			stu = UserModel.objects.values()
			student_data = list(stu)
			return JsonResponse({"status":"saved",'student_data':student_data})
		else:
			return  JsonResponse({"status":0})
def delete(request):
	if request.method == "POST":
		id = request.POST.get("sid")
		print(id)
		user = UserModel.objects.get(pk=id)
		user.delete()
		return JsonResponse({"status":1})
	else:
		return JsonResponse({"status":0})

def edit(request):
	if request.method=="POST":
		id = request.POST.get("sid")
		print(id)
		student = UserModel.objects.get(pk=id)
		student_data={'id':student.id,'name':student.name,'mobile':student.mobile,'password':student.password}
		return JsonResponse(student_data)

# def update(request):
# 	user =  request.POST.get('pid')
# 	data = UserModel.objects.filter(id=user)
# 		# name = request.POST['name']
# 		# mobile = request.POST['mobile']
# 		# password = request.POST['password']
# 		# user = UserModel(name=name,mobile=mobile,password=password)
# 		# user.save()
# 	return render(request, 'update.html',{'data':data})

