# -*- coding: utf-8 -*-

from django.db import models
from django import forms

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class PersonEditForm(forms.ModelForm):
	class Meta:
		model = Person