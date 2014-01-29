from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from common.models import News


def home(request):
    """Homepage view"""
    news = News.objects.all()[:5]
    return render(request, 'home.html', {
        'news': news,
    })


class Downloads(TemplateView):
    template_name = "common/downloads.html"

    def get_context_data(self, **kwargs):
        context = super(Downloads, self).get_context_data(**kwargs)
        context['version'] = '0.3.3'
        context['download_url'] = 'http://lutris.net/releases/'
        return context


def news_archives(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news': news})


class NewsDetails(DetailView):
    queryset = News.objects.all()
    template_name = 'common/news_details.html'
    context_object_name = 'news'

    def get_object(self):
        obj = super(NewsDetails, self).get_object()
        return obj
