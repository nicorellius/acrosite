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
from .forms import GenerateAcrosticForm
from .generate import generate_random_acrostic, generate_cute_animal_acrostic
from .constructions import adj_to_noun, adj_adj_noun_pattern, adj_to_noun_verb_adv

    
class GenerateAcrosticFormView(View):

    model = Acrostic
    form_class = GenerateAcrosticForm
    initial = {'key': 'value'}
    template_name = 'generator/generate.html'
    
    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def get(self, request):
        
        name = request.GET.get('name', '')
        
        if name != '':
            form = self.form_class(request.GET, name)
            
        else:
            form = self.form_class()
        
        print("IP address for debug-toolbar: {0}".format(request.META['REMOTE_ADDR']))
        
        return render(request, self.template_name, {'form': form})
    
    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        """
        debug for theme drop down values
        consider using messages framework instead:
            https://stackoverflow.com/questions/1463489/
        """
        theme = request.POST.get('theme-selector', '')
        print(theme)
        
        acrostic = Acrostic()
        
        print("This view is trying to create an acrostic object...")
        
        form = self.form_class(request.POST, instance=acrostic)
        
        if form.is_valid(): 
                        
            vert_word = form.cleaned_data['name']
 
            # construction = adj_to_noun(vert_word)
            # construction = adj_adj_noun_pattern(vert_word)
            construction = adj_to_noun_verb_adv(vert_word, True)
            
            # construction = Construction()
            # construction.sequence = "P;A;N;VI;AV"
            # construction.sequence = "N;VI;N;N;VI;AV"
            # construction.sequence = "A;A;NS;VS;D"

            print("Calling generate acrostic function...")
            #acrostic = generate_random_acrostic(vert_word, theme, construction)
            acrostic = generate_cute_animal_acrostic(vert_word, theme)
            # acrostic = generate_random_acrostic(vert_word)
            
            acrostic.save()
            # print("acrostic.theme: {0}".format())
                        
            if acrostic != '':
                print("Acrostic object created with vertical word '{0}' and theme '{1}'.".format(
                    request.POST['name'],
                    theme
                ))
            
            return HttpResponseRedirect('/generate/acrostic/success?theme={0}'.format(theme))
        
        return render(request, self.template_name, {
            'form': form,
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
        theme = request.GET.get('theme', '')
        
        return render(request, 'generator/success.html', {
            'acrostic': acrostic,
            'theme': theme,
        })