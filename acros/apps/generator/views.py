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

from .models import Acrostic, Construction
from .forms import GenerateAcrosticForm #@UnresolvedImport
from .generate import generate_random_acrostic
from .constructions import A_to_N, AA_N_pattern, A_to_NS_VS_D

    
class GenerateAcrosticFormView(View):
    
    form_class = GenerateAcrosticForm
    initial = {'key': 'value'}
    template_name = 'generator/generate.html'
    model = Acrostic
    
    # TODO: we may want consider using login_required decorator
    #@method_decorator(login_required)
    def get(self, request):
        
        name = request.GET.get('name', '')
        
        if name != '':
            form = self.form_class(request.GET, name)
            
        else:
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
 
            #construction = A_to_N(vert_word)
            #construction = AA_N_pattern(vert_word)
            construction = A_to_NS_VS_D(vert_word)
            
            #construction = Construction()
            #construction.sequence = "P;A;N;VI;AV"
            #construction.sequence = "N;VI;N;N;VI;AV"
            #construction.sequence = "A;A;NS;VS;D"
            acrostic = generate_random_acrostic(vert_word, construction)
            #acrostic = generate_random_acrostic(vert_word)
            
            acrostic.save()
                        
            if acrostic != '':
                print("acrostic object created with vertical word: '{0}'".format(request.POST['name']))
            
            return HttpResponseRedirect('/generate/acrostic/success/')
        
        return render(request, self.template_name, {'form': form})
    

class GenerateAcrosticSuccessView(View):

    # TODO: we may want consider using login_required decorator
    #@method_decorator(login_required)
    def get(self, request):
        
        # to fetch the `newest` item
        acrostic = Acrostic.objects.all().last() # @UndefinedVariable
        
        return render(request, 'generator/success.html', {'acrostic': acrostic})