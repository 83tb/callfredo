from django.views.decorators.csrf import csrf_exempt
from django.views.generic.simple import direct_to_template


@csrf_exempt
def phone(request):
    return direct_to_template(request, template='phonehome/default.xml')
