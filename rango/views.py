from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # modify index view，include the link to about page [cite: 1267-1268, 1284-1285]
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')