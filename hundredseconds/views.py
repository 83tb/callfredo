from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


def PlayerView(request):

    code = request.GET['code']
    return render_to_response('player.html', {'code':code })

