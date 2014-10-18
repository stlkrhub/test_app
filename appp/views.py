# Create your views here.
# -*- coding: utf-8 -*-

from django.http import HttpResponse;
from django.http import HttpResponseRedirect;
import datetime;
from django import forms
from appp.models import *
from django.shortcuts import render_to_response


def hello(request):
  return HttpResponse("Hello, World!!!" + request.get_full_path());

def get_now(request):
  return HttpResponse("<html><body>Current date/time is: %s.</body></html>" % datetime.datetime.now());

def get_now_ahead(request, offset):
  #try:
  #  offset = int(offset);
  #except ValueError:
  #  raise Http404();
  
  dt = datetime.datetime.now() + datetime.timedelta(hours = offset);
    
  return HttpResponse("<html><body>Current date/time is: %s.</body></html>" % dt);

def get_main(request):
	return HttpResponse('<html><body>		<ul>			<li><a href="/now/">Текущее время</a></li>			<li><a href="/hello/">Привет, мир!</a></li>	<li><a href="/persons/">Список персон</a></li>	<li><a href="/person_edit/">Добавить персону</a></li> </ul>		</body></html>')

def get_person_edit(request):
	if request.method == 'POST': # If the form has been submitted...
		form = PersonEditForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# Process the data in form.cleaned_data
			form.save()
			return HttpResponseRedirect('/persons/') # Redirect after POST
	else:
		form = PersonEditForm() # An unbound form

	return render_to_response('person_edit.html', {
		'form': form,
	})

def get_person_list(request):
	return HttpResponse('<html><body> </body></html>')