# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import Course
from .models import UserManager
from django.contrib import messages

def index(request):
    return redirect('/courses')


def courses(request):
    context = {
        'all_courses':Course.objects.all()
    }
    return render(request, 'course/index.html',context)
# Create your views here.

def create(request):
    
    #run validations first in models.py
    erros = Course.objects.validate(request)
    if (erros):
        print 'invalid input'
        return redirect('/courses')
    
    #then add to DB
    Course.objects.create(name=request.POST['name'],description=request.POST['description'])
    messages.success(request,"Successfully added a new course")

    #add db query here
    return redirect('/courses')

def destroy(request,id):
    context = {
        "course":Course.objects.get(id=id)
    }
    return render(request, 'course/destroy.html',context)

def delete(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/courses')