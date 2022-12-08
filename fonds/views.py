from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from fonds.models import *

def func(lst, n):
    fin_list = []
    for i in range(0, len(lst), n):
        fin_list.append(lst[i: i+n])
    return fin_list

def index(request):
    section = Section.objects.all()
    return render(request, 'fonds/index.html', {'section': section})

def category_posts(request, section_slug):
    quotes = func(Quotes.objects.all().filter(section_id__slug=section_slug), 2)
    fonds = Fonds.objects.all().filter(section_id__slug=section_slug).filter(is_published=True).prefetch_related('photos_set')
    if not fonds:
        raise Http404('Немає фондів')
    ctx = {
        'title': fonds[0].section_id.title,
        'quotes': quotes,
        'fonds': fonds,
    }
    return render(request, 'fonds/base.html', ctx)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')
