from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

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

def show(request):
    data=Employee.objects.all()
    context={'employees':data}
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

# Create your views here.
