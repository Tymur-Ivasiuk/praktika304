from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from fonds.models import *

def func(lst, n):
    fin_list = []
    for i in range(0, len(lst), n):
        fin_list.append(lst[i: i+n])
    return fin_list

def index(request):
    return render(request, 'fonds/index.html')

def zsu(request):
    quotes = func(Quotes.objects.all().filter(section_id__title="ЗСУ"), 2)
    fonds = Fonds.objects.all().filter(section_id__title="ЗСУ").filter(is_published=True).prefetch_related('photos_set')
    if not fonds:
        raise Http404('Немає фондів')
    ctx = {
        'title': "ЗСУ",
        'quotes': quotes,
        'fonds': fonds,
    }
    return render(request, 'fonds/base.html', ctx)

def support(request):
    quotes = func(Quotes.objects.all().filter(section_id__title="Підтримка"), 2)
    fonds = Fonds.objects.all().filter(section_id__title="Підтримка").prefetch_related('photos_set')
    if not fonds:
        raise Http404('Немає фондів')
    ctx = {
        'title': "Підтримка",
        'quotes': quotes,
        'fonds': fonds,
    }
    return render(request, 'fonds/base.html', ctx)

def charity(request):
    quotes = func(Quotes.objects.all().filter(section_id__title="Благодійність"), 2)
    fonds = Fonds.objects.all().filter(section_id__title="Благодійність").prefetch_related('photos_set')
    if not fonds:
        raise Http404('Немає фондів')
    ctx = {
        'title': "Благодійність",
        'quotes': quotes,
        'fonds': fonds,
    }
    return render(request, 'fonds/base.html', ctx)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')
