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

from .models import Word, Acrostic
from .forms import GenerateAcrosticForm

    
class GenerateAcrosticFormView(View):
    
    form_class = GenerateAcrosticForm
    initial = {'key': 'value'}
    template_name = 'generator/generate.html'
    model = Word
    #model = Acrostic #need to set the model here, that way .save() method works, also update database
    
    # TODO: we may want consider using login_required decorator
    #@method_decorator(login_required)
    def get(self, request):
        
        form = self.form_class()
        
        print("ip address for debug-toolbar: {0}".format(request.META['REMOTE_ADDR']))
        
        return render(request, self.template_name, {'form': form})
    
    # TODO: we may want consider using login_required decorator
    #@method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        
        word = Word()
        #acrostic = Acrostic()
        
        print("this view is trying to create a word object...")
        
        form = self.form_class(request.POST, instance=word)
        
        if form.is_valid(): 
                        
            name = form.cleaned_data['name']

            #vert_word = form.cleaned_data['name']

            #acrostic.generate_random_acrostic(vert_word)
            #acrostic.save()
           
            word.generate_acrostic()
            #word.acrostic_text = acrostic.component_words
            word.save()
            
            if word != '':
                print("word name: '{0}'".format(request.POST['name']))
                print("word acrostic text: '{0}'".format(word.acrostic_text))
            
            return HttpResponseRedirect('/generate/success/')
        
        return render(request, self.template_name, {'form': form})
    

 
class GenerateAcrosticSuccessView(View):

    # TODO: we may want consider using login_required decorator
    #@method_decorator(login_required)
    def get(self, request):
        
        #words = Word.objects.all() # to fetch all objects
        # to fetch the `newest` item
        word = Word.objects.all().last()
        
        return render(request, 'generator/success.html', {'word': word})