from django.shortcuts import render

def index(request):

    # if there is a POST request we need to process the form data
    if request.method == 'POST':

        poem = request.POST.get('poemInput')

        context = {
            'poem': poem,
        }
    else:
        context = {}

    return render(request, 'detection/home.html', context)
