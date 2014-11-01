"""
file        :   views.py
date        :   2014-1101
module      :   generator
classes     :   GeneratorView, GeneratorFormView
desription  :   views for word generator
"""

from django.shortcuts import render
from django.views.generic.base import View

from .models import Word
from .forms import GenerateAcrosticForm



class GenerateAcrosticView(View):
    
    # TODO: we may want consider using login_required decorator
    #@method_decorator(login_required)
    def get(self, request):
        
        words = get_object_or_404(Word)
        
        return render(request, 'index.html', {
            'words': words,
        })


    
class GenerateAcrosticFormView(View):
    
    form_class = GenerateAcrosticForm
    initial = {'key': 'value'}
    template_name = 'index.html'
    model = Word
    
    # TODO: we may want consider using login_required decorator
    #@method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        
        word = Word()
        
        form = self.form_class(request.POST, instance=word)
        
        print('name of current word object: ' + request.POST['word'])
        
        if form.is_valid(): 
            
            word = form.cleaned_data['word']
            
            document.owner = request.user
            document.name = name
            document.docfile = docfile
            document.description = description
            
            document.save()
            
            self.send_upload_file_completed_message(request)
            
            return HttpResponseRedirect('/generate/success/')
        
        return render(request, self.template_name, {'form': form})
    


class GenerateAcrosticSuccessView(View):

    # TODO: we may want consider using login_required decorator
    #@method_decorator(login_required)
    def get(self, request):
        
        return render(request, 'index.html')