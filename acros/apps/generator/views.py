"""
file         :   views.py
date         :   2014-11-01
module       :   generator
classes      :   GeneratorView, GeneratorFormView
description  :   views for word generator
"""
import re
import json
import numpy

from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.text import slugify

from .models import Acrostic, Score
from .forms import GenerateAcrosticForm
from .generate import generate_random_acrostic
from .constructions import adj_to_noun_sin_verb_sin_adj

    
class GenerateAcrosticFormView(View):
    
    form_class = GenerateAcrosticForm
    initial = {'key': 'value'}
    template_name = 'generator/generate.html'
    model = Acrostic
    
    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def get(self, request):
        
        name = request.GET.get('name', '')
        theme = request.GET.get('theme', '')
        ecrostic = request.GET.get('ecrostic', '')

        print('get name: {0}'.format(name))
        print('get theme: {0}'.format(theme))
        print('get acrostic: {0}'.format(ecrostic))
        
        if name != '':
            form = self.form_class(request.GET)
            
        else:
            form = self.form_class()
        
        print("ip address for debug-toolbar: {0}".format(request.META['REMOTE_ADDR']))
        
        return render(request, self.template_name, {'form': form})
    
    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def post(self, request):

        name = request.POST.get('name', '')
        theme = request.POST.get('theme', '')
        
        print("this view is trying to create an acrostic object...")
        print('post name: {0}'.format(name))
        print('post theme: {0}'.format(theme))
        
        form = self.form_class(request.POST)
        
        if form.is_valid():

            if name != '':
                vert_word = name

            else:
                vert_word = form.cleaned_data['name']

            construction = adj_to_noun_sin_verb_sin_adj(vert_word)

            acrostic = generate_random_acrostic(vert_word, construction)
            slug = slugify(re.sub(';', ' ', acrostic.horizontal_words))
            acrostic.slug = slug
            acrostic.save()
                        
            if acrostic != '':
                print("acrostic object created with vertical word: '{0}'".format(request.POST['name']))

            if not request.is_ajax():
                return HttpResponseRedirect('/generate/acrostic/?name={0}&theme={1}'.format(
                    vert_word,
                    theme,
                ))
            # else:
            #     response_data = {
            #         'status': 'debug',
            #         'message': 'this view is using an ajax response'
            #     }
            #
            #     return HttpResponse(json.dumps(response_data), content_type="application/json")
            #     return HttpResponse("Text only, please.", content_type="text/plain")

        return render(request, self.template_name, {
            'form': form,
            'theme': theme,
        })
    

class GenerateAcrosticSuccessView(View):

    template_name = 'generator/success.html'
    model = Acrostic

    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def get(self, request):
        
        # this fetches the newest object
        acrostic = Acrostic.objects.all().last()

        # consider using messages framework instead:
        #     https://stackoverflow.com/questions/1463489/
        theme = request.GET.get('theme', '')
        
        return render(request, self.template_name, {
            'acrostic': acrostic,
            'theme': theme,
        })


class RateAcrosticView(View):

    template_name = 'generator/success.html'
    model = Acrostic

    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def get(self, request):

        value = request.GET.get('value', '')
        print('here is value of star rating: {0}'.format(value))

        return render(request, self.template_name, {
            'value': value
        })

    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def post(self, request):

        star_value = request.POST.get('value', '')
        print('value of star rating: {0}'.format(star_value))

        acrostic = Acrostic.objects.all().last()

        score = Score()
        score.acrostic = acrostic
        score.value = star_value
        score.save()

        score_objects = acrostic.score_set.all()
        scores = []
        for score in score_objects:
            # print(score.value)
            scores.append(score.value)

        average = round(numpy.mean(scores), 1)
        total = len(score_objects)

        # score.mean = numpy.mean(scores)
        # score.total = len(score_objects)
        # score.save()

        print('scores: {0}'.format(scores))
        print('average: {0}'.format(average))

        xhr = 'xhr' in request.GET
        print('XHR in request: {0}'.format(xhr))

        response_data = {
            'message': 'value of star rating:',
            'value': star_value,
            'average': average,
            'total': total
        }

        if xhr and star_value:
            response_data.update({'success': True})

        else:
            response_data.update({'success': False})

        if xhr:
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        return render_to_response(self.template_name, response_data)