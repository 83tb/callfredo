from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class PlayerView(TemplateView):
    template_name = 'player.html'