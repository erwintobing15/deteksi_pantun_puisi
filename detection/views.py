from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('detection/index.html')
    context = {
        'page': "Halaman index",
    }
    return HttpResponse(template.render(context, request))
