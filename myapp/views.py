from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView
from django.core.mail import send_mail
from django.contrib.auth.mixins import UserPassesTestMixin
from rest_framework import viewsets
from .serializers import EmployeeSerializers

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

def restaurant(request):
    if request.method == 'POST':
        name=request.POST['name']
        number=request.POST['number']
        street=request.POST['street']
        city=request.POST['city']
        zipcode=request.POST['zipcode']
        state=request.POST['state']
        country=request.POST['country']
        telephone=request.POST['telephone']
        restObj = Restaurant(
            name= name,
            number= number,
            street= street,
            city= city,
            zipcode= zipcode,
            state= state,
            country= country,
            telephone= telephone)
        restObj.save()
        return redirect('/myapp/Restaurant/Show')
    return render(request,'restaurant.html')

def dish(request):
    if request.method == 'POST':
        res=request.POST['name1']
        name=request.POST['name']
        description=request.POST['description']
        price=request.POST['price']
        qw=Restaurant.objects.get(id=res)
        print(qw)
        dishobj=Dish(
            name=name,
            description=description,
            price=price,
            restaurant=qw
            )
        dishobj.save()
        return redirect('/myapp/dish')
    obj=Restaurant.objects.all()
    context={'name':obj}
    return render(request,'dish.html',context)

def review(request):
    if request.method=='POST':
        a= request.POST['rating_choice'],
        b= request.POST['description']
        print(a,b)
        object=Review(rating=int(a[0]), comment=b)
        object.save()
        return render(request, 'review.html')
    return render(request,'review.html')

def restaurantShow(request):
    res=Restaurant.objects.all()
    context={'restro':res}
    return render(request,'restaurantShow.html',context)

def showall(request):
    rest=Restaurant.objects.all()
    context={'restaurants': rest}
    return render(request,'restauranttotal.html',context)

def delete(request,id):
    obj = Restaurant.objects.get(id=id)
    obj.delete()
    return redirect('/myapp/Restaurant/Show/')

def update(request,id):
    if request.method=='POST':
        restaurant(request)
    obj = Restaurant.objects.get(id=id)
    context_new = {'Restro':obj}
    return render(request,'update.html', context_new)

def student(request):
    if request.method=='POST':
        a=request.POST['name']
        r=Student(name=a)
        r.save()
        return render(request,'student.html')
    return render (request,'student.html')

def index(request):
    if request.method=='POST':
        form=Nameform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/myapp/show')
        else:
            return HttpResponse('<h1> THE DECIMATION</h1>')
    else:
        form=Nameform()
    content={'form':form}
    return render(request, 'forms.html', content)

@login_required()
def show(request):
    profile_list = Employee.objects.all()
    paginator = Paginator(profile_list, 2)
    page= request.GET.get('page')
    posts = paginator.get_page(page)
#    data=Employee.objects.all()
    context={'employees':posts}
    print(paginator.page_range)
    return render(request, 'show.html', context)

def delete(request,id):
    data=Employee.objects.get(id=id)
    data.delete()
    messages.error(request,f'message has been deleted {id}')
    return redirect('/myapp/show')


def update(request,id):
    data=Employee.objects.get(id=id)
    emp=Nameform(instance=data)
    context={'form':emp}
    return render(request,'forms.html', context)

def search(request):
    search_box=request.POST['searching']
    data=Employee.objects.filter(emp_name__icontains=search_box)
    context={'employees': data}
    return render(request, 'show.html', context)

def register(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
           form1=userform(request.POST)
           if form1.is_valid():
               username=form1.cleaned_data['username']
               first_name = form1.cleaned_data['first_name']
               last_name = form1.cleaned_data['last_name']
               email = form1.cleaned_data['email']
               password = form1.cleaned_data['password']
               User.objects.create_user(username=username,
               first_name=first_name,last_name=last_name,
               email=email,password=password)
               send_mail(
                'Dayum',
                'hello you Fuckked up',
                'alindjain13@gmail.com',
                [email],
                fail_silently=False,
               )
               return redirect('myapp/registeration')
        else:
            form1=userform()
        context = {'form':form1}
        return render(request,'registration.html',context)
    return HttpResponse('Already registered')


def loging(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/myapp/show/')
            else:
                return HttpResponse('<h1> NOPE </h1>')
        return render(request, 'login.html')
    else:
        return HttpResponse('Already logged IN')

def logoutuser(request):
    logout(request)
    return render(request, 'login.html')


def changepass(request):
    user=request.userform
    if request.method=='POST':
        form = ChangePassword(request.POST)
        if form.is_valid():
            new_password=form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            return redirect('login/')
        else:
            form= ChangePassword()
    return render(request, 'password.html', {'form':form})

class HomeView(TemplateView):
    template_name='about.html'

class EmployeeListView(ListView):
    template_name='show2.html'
    model = Employee

    #queryset=Employee.objects.all()
    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        qs1 = Employee.objects.all()
        context.update({'users': qs1})
        return context

class Detail(DetailView):
    template_name='employeelist.html'
    #queryset=Employee.objects.all()
    def get_object(self):
        id_ = self.kwargs.get('emp_id')
        return get_object_or_404(Employee, emp_id=id_)

class EmployeeAdd(CreateView):
    template_name = 'employeeadd.html'
    form_class = Nameform
    queryset = Employee.objects.all()

# def employees_data(request):
#     a=Employee.objects.order_by('-emp_name')[:]
#     num_visit = request.session.get('-num_visit',1)
#     print(num_visit)
#     request.session['num_visit']=num_visit+1
#     return render(request, 'employees_data.html',{'record':a, 'nv':num_visit})



# class Employeeupdate(UserPassesTestMaxin, UpdateView):
#     model=Employee
#     fields= ['emp_name']
#
#     def test_func(self):
#         employee= self.get_object()
#         return employee,id=seld.user.id
#
#
#
# Create your views here.
