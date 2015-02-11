"""
file        :   views.py
date        :   2015-02-11
module      :   search
classes     :
description :   Search word database
"""

from django.http import HttpResponseRedirect
from django.shortcuts import render

from apps.generator.models import Word


def search(request):
    query = request.GET.get('q', '')
    word_results = []
    results = []
    
    if query:
        word_results = Word.objects.filter(
            searchkeyword__keyword__in=query.split()).distinct()

    if len(word_results) == 1:
        return HttpResponseRedirect(word_results[0].get_absolute_url())

    results.append(Word.objects.filter(content__icontains=query))

    # TODO - consider return render_to_response( # replace with 'return render(request'
    # see this post: http://stackoverflow.com/questions/6261823/
    # and this one: http://stackoverflow.com/questions/6740112/
    
    return render(
        request, 'search/search.html', {
            'query': query,
            'keyword_results': word_results,
            'results': results
        }
    )
