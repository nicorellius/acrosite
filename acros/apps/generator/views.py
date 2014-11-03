"""
file        :   views.py
date        :   2014-1101
module      :   generator
classes     :   GeneratorView, GeneratorFormView
desription  :   views for word generator
"""

from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponseRedirect

from .models import Word
from .forms import GenerateAcrosticForm


    
class GenerateAcrosticFormView(View):
    
    form_class = GenerateAcrosticForm
    initial = {'key': 'value'}
    template_name = 'generator/generate.html'
    model = Word
    
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
        
        print("this view is trying to create a word object...")
        
        form = self.form_class(request.POST, instance=word)
        
        print('word object created: {0}'.format(request.POST['name']))
        
        if form.is_valid(): 
            
            name = form.cleaned_data['name']
            
            word.save()
            
            return HttpResponseRedirect('/generate/success/')
        
        return render(request, self.template_name, {'form': form})
    


class GenerateAcrosticSuccessView(View):

    # TODO: we may want consider using login_required decorator
    #@method_decorator(login_required)
    def get(self, request):
        
        words = Word.objects.all()
        
        return render(request, 'generator/success.html', {'words': words})