
from django.urls import path, include
#from django.conf import settings
#from django.conf.urls.static import static
#from django.views.generic import TemplateView,ListView
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', EmployeeViewSet)


urlpatterns = [
    path('employee/', include(router.urls)),



]
