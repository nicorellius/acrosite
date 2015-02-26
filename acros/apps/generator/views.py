"""
file         :   views.py
date         :   2014-11-01
module       :   generator
classes      :   GeneratorView, GeneratorFormView
description  :   views for word generator
"""
import re
import json
# import numpy
import logging

from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
# from django.utils.text import slugify

from common.util import get_timestamp
from apps.generator.templatetags.custom import slagify
# from common.signals import ecrostic_not_found

from .models import Acrostic, Score
from .forms import GenerateAcrosticForm
from .generate import generate_random_acrostic


logger = logging.getLogger(__name__)


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

        logger.info("{0}: GET name: {1}".format(get_timestamp(), name))
        logger.info("{0}: GET theme: {1}".format(get_timestamp(), theme))
        
        if name != '':
            form = self.form_class(request.GET)
            
        else:
            form = self.form_class()

        logger.info("{0}: IP address for debug-toolbar: {1}".format(get_timestamp(), request.META['REMOTE_ADDR']))
        
        return render(request, self.template_name, {'form': form})
    
    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def post(self, request):

        name = request.POST.get('name', '')
        theme = request.POST.get('theme', '')
        
        logger.info("{0}: This view is trying to create an acrostic object...".format(get_timestamp()))
        logger.info("{0}: POST name: {1}".format(get_timestamp(), name))
        logger.info("{0}: POST theme: {1}".format(get_timestamp(), theme))

        form = self.form_class(request.POST)

        if form.is_valid():

            if name != '':
                vert_word = name

            else:
                vert_word = form.cleaned_data['name']

            acrostic = generate_random_acrostic(vert_word, theme)
            # using custom templatetag `slagify` which leaves in punctuation
            # word_list = acrostic.horizontal_words.split(';')
            # for word in word_list:
            #     if '-' in word:
            #         print('Word has hyphen: {0}'.format(word))
            # slug = slagify(re.sub(';', ' ', acrostic.horizontal_words))
            # acrostic.slug = slug
            # TODO - create generate uri function to add DRY-ness to code on this acrostic_uri bit
            acrostic_uri = re.sub(' ', '+', acrostic.horizontal_words)
            acrostic_uri = re.sub(';', '_', acrostic_uri)
            acrostic_uri = acrostic_uri[:-1]
            logger.info("{0}: Horizontal words: {1}".format(get_timestamp(), acrostic.horizontal_words))
            acrostic.save()

            if not request.is_ajax():
                return HttpResponseRedirect('/generate/acrostic/?name={0}&theme={1}&ecrostic={2}'.format(
                    vert_word,
                    theme,
                    acrostic_uri
                ))

            #########################################################################################
            # TODO - sort this out. this works only because I'm pushing an URL without the ecrostic
            # TODO - need to figure out how to get that damn ecrostic into this script.
            # xhr = 'xhr' in request.GET
            # logger.info("{0}: XHR in request: {1}".format(get_timestamp(), xhr))
            #
            # if xhr:
            #     data = serializers.serialize('json', [acrostic, ], fields='slug')
            #     return HttpResponse(json.dumps(data), content_type="application/json")
            #
            #########################################################################################

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

        logger.info("{0}: GET score data: {1}".format(get_timestamp(), scores))
        logger.info("{0}: GET score mean data: {1}".format(get_timestamp(), score_means))
        logger.info("{0}: GET score total data: {1}".format(get_timestamp(), score_totals))

        name = request.GET.get('name', '')
        theme = request.GET.get('theme', '')
        ecrostic = request.GET.get('ecrostic', '')

        logger.info("{0}: GET name: {1}".format(get_timestamp(), name))
        logger.info("{0}: GET theme: {1}".format(get_timestamp(), theme))
        logger.info("{0}: GET ecrostic: {1}".format(get_timestamp(), ecrostic))
        logger.info("{0}: Current acrostic: {1}".format(get_timestamp(), acrostic.horizontal_words))

        ecrostic_string = '{0};'.format(re.sub('_', ';', ecrostic))
        pseudo_ecrostic = re.sub('_', ' ', ecrostic)
        level_acrostic = re.sub(';', ' ', acrostic.horizontal_words)

        acrostic_uri = re.sub(' ', '+', acrostic.horizontal_words)
        acrostic_uri = re.sub(';', '_', acrostic_uri)
        acrostic_uri = acrostic_uri[:-1]

        logger.info("{0}: Acrostic string (sub hyphens for semi-colons): {1}".format(get_timestamp(), ecrostic_string))
        logger.info("{0}: Pseudo ecrostic (sub hyphens for spaces): {1}".format(get_timestamp(), pseudo_ecrostic))
        logger.info("{0}: Level acrostic (words separated by spaces): {1}".format(get_timestamp(), level_acrostic))
        logger.info("{0}: Acrostic URI fragment (browser friendly): {1}".format(get_timestamp(), acrostic_uri))

        # TODO - find a better way to check if acrostic exists!
        if Acrostic.objects.filter(horizontal_words=ecrostic_string).exists():

            return render(request, self.template_name, {
                'acrostic': acrostic,
                'acrostic_uri': acrostic_uri,
                'pseudo_ecrostic': pseudo_ecrostic,
                'name': name,
                'theme': theme,
                'scores': scores,
                'score_means': score_means,
                'score_totals': score_totals
            })

        elif not Acrostic.objects.filter(horizontal_words=ecrostic_string).exists():

            if ecrostic == '':

                return render(request, self.template_name, {
                    'acrostic': acrostic,
                    'acrostic_uri': acrostic_uri,
                    'pseudo_ecrostic': pseudo_ecrostic,
                    'name': name,
                    'theme': theme,
                    'scores': scores,
                    'score_means': score_means,
                    'score_totals': score_totals
                })

            logger.info("{0}: Ecrostic `{1}` not found.".format(get_timestamp(), pseudo_ecrostic))
            messages.add_message(request, messages.INFO, '{0}'.format(pseudo_ecrostic))

            return HttpResponseRedirect('/generate/')

        return render(request, self.template_name, {
            'acrostic': acrostic,
            'acrostic_uri': acrostic_uri,
            'pseudo_ecrostic': pseudo_ecrostic,
            'name': name,
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
        logger.info("{0}: GET here is value of the current star rating: {1}".format(get_timestamp(), star_value))

        score = Score.objects.all().last()
        logger.info("{0}: Mean score for this get request: {1}".format(get_timestamp(), score.mean))
        logger.info("{0}: Total number of scores reported for this request: {1}".format(get_timestamp(), score.total))

        return render(request, self.template_name, {
            'value': star_value,
            'score': score
        })

    # TODO: we may want consider using login_required decorator
    # @method_decorator(login_required)
    def post(self, request):

        star_value = request.POST.get('value', '')
        logger.info("{0}: POST value of the current star rating: {1}".format(get_timestamp(), star_value))

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
        # average = round(numpy.mean(scores), 1)
        average = round(float(sum(scores))/len(scores) if len(scores) > 0 else float('nan'), 1)
        total = len(score_objects)

        # save averages and totals to database
        score.mean = average
        score.total = total
        score.save()

        logger.info("{0}: Scores: {1}".format(get_timestamp(), scores))
        logger.info("{0}: Average: {1}".format(get_timestamp(), average))

        xhr = 'xhr' in request.GET
        logger.info("{0}: XHR in request: {1}".format(get_timestamp(), xhr))

        response_data = {
            'message': 'Statistics for star rating',
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
