from django.shortcuts import render

from .svm.classifier import get_poem_type, get_poem_probability

def index(request):

    # if there is a POST request we need to process the form data
    if request.method == 'POST':

        poem = request.POST.get('poemInput')
        poem_type = get_poem_type(poem) if get_poem_type(poem) else "";
        # get poem_proba based on poem_type pantun or puisi
        poem_proba = get_poem_probability(poem)
        if poem_type == "pantun":
            poem_proba = poem_proba[0][0]
        elif poem_type == "puisi":
            poem_proba = poem_proba[0][1]
        else:
            poem_proba = 0
        poem_proba = int(poem_proba*100)

        context = {
            'poem': poem,
            'poem_type': poem_type,
            'probability': poem_proba,
        }
    else:
        context = {}

    return render(request, 'detection/home.html', context)
