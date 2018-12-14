from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields= ('emp_name', 'competency')
