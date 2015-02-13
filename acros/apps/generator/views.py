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
import logging

from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.text import slugify

from common.util import get_timestamp

from .models import Acrostic, Score
from .forms import GenerateAcrosticForm
from .generate import generate_random_acrostic


logger = logging.getLogger(__name__)

timestamp = get_timestamp()


class GenerateAcrosticFormView(View):

    model = Acrostic
    form_class = GenerateAcrosticForm
    initial = {'key': 'value'}
    template_name = 'generator/generate.html'
    
    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def get(self, request):
        
        name = request.GET.get('name', '')
        theme = request.GET.get('theme', '')
        ecrostic = request.GET.get('ecrostic', '')

        logger.info("{0}: get name: {1}".format(timestamp, name))
        logger.info("{0}: get theme: {1}".format(timestamp, theme))
        logger.info("{0}: get acrostic: {1}".format(timestamp, ecrostic))
        
        if name != '':
            form = self.form_class(request.GET)
            
        else:
            form = self.form_class()

        logger.info("{0}: ip address for debug-toolbar: {1}".format(timestamp, request.META['REMOTE_ADDR']))
        
        return render(request, self.template_name, {'form': form})
    
    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def post(self, request):

        name = request.POST.get('name', '')
        theme = request.POST.get('theme', '')
        
        logger.info("{0}: this view is trying to create an acrostic object...".format(timestamp))
        logger.info("{0}: post name: {1}".format(timestamp, name))
        logger.info("{0}: post theme: {1}".format(timestamp, theme))

        form = self.form_class(request.POST)

        if form.is_valid():

            if name != '':
                vert_word = name

            else:
                vert_word = form.cleaned_data['name']

            acrostic = generate_random_acrostic(vert_word, theme)
            slug = slugify(re.sub(';', ' ', acrostic.horizontal_words))
            acrostic.slug = slug
            acrostic.save()

            """
            # using get_or_create() in generate to check for existing acrostic
            # https://docs.djangoproject.com/en/1.7/ref/models/querysets/#get-or-create
            acrostic_exists = Acrostic.objects.filter(horizontal_words=acrostic.horizontal_words).exists()
            if acrostic_exists:
                print("acrostic matched: {0}".format(acrostic))
            """

            if not request.is_ajax():
                return HttpResponseRedirect('/generate/acrostic/?name={0}&theme={1}&ecrostic={2}'.format(
                    vert_word,
                    theme,
                    acrostic.slug
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

        acrostic = Acrostic.objects.all().last()
        score_data = acrostic.score_set.all()
        scores = []
        score_means = []
        score_totals = []

        for score_datum in score_data:
            scores.append(score_datum.value)
            score_means.append(score_datum.mean)
            score_totals.append(score_datum.total)

        logger.info("{0}: GET score data: {1}".format(timestamp, scores))
        logger.info("{0}: GET score mean data: {1}".format(timestamp, score_means))
        logger.info("{0}: GET score total data: {1}".format(timestamp, score_totals))

        theme = request.GET.get('theme', '')
        
        return render(request, self.template_name, {
            'acrostic': acrostic,
            'theme': theme,
            'scores': scores,
            'score_means': score_means,
            'score_totals': score_totals
        })


class RateAcrosticView(View):

    template_name = 'generator/success.html'
    model = Acrostic

    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def get(self, request):

        star_value = request.GET.get('value', '')
        logger.info("{0}: GET here is value of the current star rating: {1}".format(timestamp, star_value))

        score = Score.objects.all().last()
        logger.info("{0}: mean score for this get request: {1}".format(timestamp, score.mean))
        logger.info("{0}: total number of scores reported for this get request: {1}".format(timestamp, score.total))

        return render(request, self.template_name, {
            'value': star_value,
            'score': score
        })

    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def post(self, request):

        star_value = request.POST.get('value', '')
        logger.info("{0}: POST here is value of the current star rating: {1}".format(timestamp, star_value))

        acrostic = Acrostic.objects.all().last()

        score = Score()
        score.acrostic = acrostic
        score.value = star_value
        score.save()

        score_objects = acrostic.score_set.all()
        scores = []
        for score_object in score_objects:
            # print(score.value)
            scores.append(score_object.value)

        # calculate averages and totals
        average = round(numpy.mean(scores), 1)
        total = len(score_objects)

        # save averages and totals to database
        score.mean = average
        score.total = total
        score.save()

        logger.info("{0}: scores: {1}".format(timestamp, scores))
        logger.info("{0}: average: {1}".format(timestamp, average))

        xhr = 'xhr' in request.GET
        logger.info("{0}: XHR in request: {1}".format(timestamp, xhr))

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