"""
file         :   views.py
date         :   2014-11-01
module       :   generator
classes      :   GeneratorView, GeneratorFormView
description  :   views for word generator
"""

from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponseRedirect

from .models import Acrostic
from .forms import GenerateAcrosticForm # @UnresolvedImport

    
class GenerateAcrosticFormView(View):
    
    form_class = GenerateAcrosticForm
    initial = {'key': 'value'}
    template_name = 'generator/generate.html'
    model = Acrostic
    
    # TODO: we may want consider using login_required decorator
    #@method_decorator(login_required)
    def get(self, request):
        
        form = self.form_class()
        
        print("ip address for debug-toolbar: {0}".format(request.META['REMOTE_ADDR']))
        
        return render(request, self.template_name, {'form': form})
    
    # TODO: we may want consider using login_required decorator
    #@method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        
        acrostic = Acrostic()
        
        print("this view is trying to create an acrostic object...")
        
        form = self.form_class(request.POST, instance=acrostic)
        
        if form.is_valid(): 
                        
            vert_word = form.cleaned_data['name']
            acrostic = Acrostic()
            acrostic.generate_random_acrostic(vert_word)
            acrostic.save()
            
            if acrostic != '':
                print("acrostic object created with vertical word: '{0}'".format(request.POST['name']))
            
            return HttpResponseRedirect('/generate/success/')
        
        return render(request, self.template_name, {'form': form})
    

 
class GenerateAcrosticSuccessView(View):

    # TODO: we may want consider using login_required decorator
    #@method_decorator(login_required)
    def get(self, request):
        
        # to fetch the `newest` item
        acrostic = Acrostic.objects.all().last()  # @UndefinedVariable
        
        return render(request, 'generator/success.html', {'acrostic': acrostic})