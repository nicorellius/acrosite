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

from .models import Acrostic, Theme
from .forms import GenerateAcrosticForm
from .generate import generate_random_acrostic
from .constructions import adj_to_noun, adj_adj_noun_pattern, adj_to_noun_sin_verb_sin_adj

    
class GenerateAcrosticFormView(View):
    
    form_class = GenerateAcrosticForm
    initial = {'key': 'value'}
    template_name = 'generator/generate.html'
    model = Acrostic
    
    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def get(self, request):
        
        name = request.GET.get('name', '')
        
        if name != '':
            form = self.form_class(request.GET, name)
            
        else:
            form = self.form_class()
        
        print("ip address for debug-toolbar: {0}".format(request.META['REMOTE_ADDR']))
        
        return render(request, self.template_name, {'form': form})
    
    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        """
        debug for theme drop down values
        consider using messages framework instead:
            https://stackoverflow.com/questions/1463489/
        """
        ts = request.POST.get('theme-selector', '')
        print(ts)
        
        acrostic = Acrostic()
        theme = Theme()
        
        print("this view is trying to create an acrostic object...")
        
        form = self.form_class(request.POST, instance=acrostic)
        
        if form.is_valid(): 
                        
            vert_word = form.cleaned_data['name']
 
            # construction = adj_to_noun(vert_word)
            # construction = adj_adj_noun_pattern(vert_word)
            construction = adj_to_noun_sin_verb_sin_adj(vert_word)
            
            # construction = Construction()
            # construction.sequence = "P;A;N;VI;AV"
            # construction.sequence = "N;VI;N;N;VI;AV"
            # construction.sequence = "A;A;NS;VS;D"
            acrostic = generate_random_acrostic(vert_word, construction)
            # acrostic = generate_random_acrostic(vert_word)
            
            acrostic.save()

            theme.name = ts  # form.cleaned_data['theme-selector']
            theme.save()
                        
            if acrostic != '':
                print("acrostic object created with vertical word: '{0}'".format(request.POST['name']))
            
            return HttpResponseRedirect('/generate/acrostic/success/?theme={0}'.format(ts))
        
        return render(request, self.template_name, {
            'form': form,
            'theme-selector': ts,
            'theme': theme,
        })
    

class GenerateAcrosticSuccessView(View):

    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def get(self, request):
        
        # to fetch the `newest` item
        acrostic = Acrostic.objects.all().last()

        # consider using messages framework instead:
        #     https://stackoverflow.com/questions/1463489/
        ts = request.GET.get('theme', '')
        
        return render(request, 'generator/success.html', {
            'acrostic': acrostic,
            'ts': ts,
        })