from django.views.generic.base import TemplateView

TEMPLATES_DIR = 'accounts/'

class SocialErrorView(TemplateView):
    template_name = TEMPLATES_DIR + 'error.html'
