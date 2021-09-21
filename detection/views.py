from django.shortcuts import render

from .svm.classifier import get_poem_type

def index(request):

    # if there is a POST request we need to process the form data
    if request.method == 'POST':

        poem = request.POST.get('poemInput')
        poem_type = get_poem_type(poem) if get_poem_type(poem) else "";

        context = {
            'poem': poem,
            'poem_type': poem_type,
        }
    else:
        context = {}

    return render(request, 'detection/home.html', context)
