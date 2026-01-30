from django.http import HttpResponse

def index(request):
    # modify index view，include the link to about page [cite: 1267-1268, 1284-1285]
    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

def about(request):
    # create about view，include the link to the homepage  [cite: 1264, 1269, 1286-1287]
    return HttpResponse("Rango says here is the about page. <br/> <a href='/rango/'>Index</a>")