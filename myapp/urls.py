
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView,ListView
from .views import *

urlpatterns = [
    path('Restaurant/', restaurant, name='restro'),
    path('Dish/', dish),
    path('forms/', index, name='add'),
    path('review/', review),
    path('Restaurant/Show', restaurantShow),
    path('Restaurant/total', showall),
    path('delete/<int:id>', delete,name='delete'),
    path('update/<int:id>', update,name='update'),
    path('student',student,name='student'),
    path('show/', show, name='show'),
    path('search/', search, name='search'),
    path('registration/', register, name='register'),
    path('login/', loging, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('changepassword/', changepass, name='password'),
    path('home/', HomeView.as_view(), name='home'),
    path('employee/', EmployeeListView.as_view(), name='employs')

]
