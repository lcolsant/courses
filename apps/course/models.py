# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

# Create your models here.
class UserManager(models.Manager):
    def validate(self,request):
        errors = False
        if len(request.POST['name']) < 2:
            messages.error(request,"Course name should be more than 1 characters")
            errors = True
        if request.POST['description'] == "":
            messages.error(request,"You need to enter a description")
            errors = True
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return "<Course object: {} {}>".format(self.name,self.description)
