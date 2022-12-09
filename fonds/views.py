from django.http import HttpResponseNotFound, Http404
from django.views.generic import TemplateView, ListView

from fonds.models import *
from fonds.functions import quotes_slicer

class HomeView(TemplateView):
    template_name = 'fonds/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['section'] = Section.objects.all()
        return ctx


class CategoryView(ListView):
    model = Fonds
    template_name = 'fonds/base.html'
    context_object_name = 'fonds'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Section.objects.get(slug=self.kwargs['section_slug']).title
        context['quotes'] = quotes_slicer(Quotes.objects.all().filter(section_id__slug=self.kwargs['section_slug']), 2)
        return context

    def get_queryset(self):
        fonds = Fonds.objects.all().filter(section_id__slug=self.kwargs['section_slug'], is_published=True).prefetch_related('photos_set')
        if not fonds:
            raise Http404()

        return fonds


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')
