"""
file        :   views.py
date        :   2015-02-11
module      :   search
classes     :
description :   Search word database
"""

import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q

from apps.generator.models import Word

from common.util import get_timestamp


logger = logging.getLogger(__name__)

timestamp = get_timestamp()


class WordListSearchView(View):

    def get(self, request):

        query = request.GET.get('q', '')

        if query:

            result = Word.objects.filter(name__icontains=query)

            logger.info("{0} Found a word search match for {1}".format(timestamp, result))

            return render(request, 'search/search.html', {
                'result': result,
                'query': query
            })

        return render(
            request, 'search/search.html', {
                'query': query,
                'result': 'none'
            }
        )
