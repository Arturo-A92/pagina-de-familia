from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

from firstview.models import Papa, Mama, Herma

def inicio(request):
    
    template1 = loader.get_template("inicio.html")

    render1 = template1.render({})

    return HttpResponse(render1)

def padre(request):

    template1 = loader.get_template("familia.html")
    papa = Papa(nombre='Alfredo', edad=64, fecha_nacimiento = '16-04-1958')
    render1 = template1.render({'papa':papa })

    return HttpResponse(render1)

def madre(request):

    template1 = loader.get_template("madre.html")
    mama = Mama(nombre='Aleida', edad=60, fecha_nacimiento = '16-03-1962')
    render1 = template1.render({'mama':mama})
    return HttpResponse(render1)

def hermana(request):

    template1 = loader.get_template("hermana.html")
    hermana = Herma(nombre='Albadis', edad=33, fecha_nacimiento = '09-12-1988')
    render1 = template1.render({'hermana':hermana})

    return HttpResponse(render1)