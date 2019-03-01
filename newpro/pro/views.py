# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            Hostname = form.cleaned_data.get('your_name')
            Package = form.cleaned_data.get('your_package')
            context = {'Hostname':Hostname,'Package':Package}
            import os
            f = open( '/root/hostname', 'w+' )
            f.write( Hostname )
            f.close()
            f = open( '/root/indata', 'w+' )
            f.write( Package )
            f.close()  
            cmd = 'ansible-playbook /hostname.yml'
            os.system(cmd)
            cmd1 = 'ansible-playbook /install.yml'
            os.system(cmd1)
            return render(request, 'name.html',context)
            #template = loader.get_template('showdata.html')
            #return HttpResponseRedirect(template.render(context,request))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

#def index(request):
#   return HttpResponse("Hello, world. You're at my website")
