from django.shortcuts import render
from django.http import HttpResponse
import datetime

from teste.models import Animal

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    animais = Animal.objects.all()
    print(list(animais))
    html = "<html><body>It is now %s." % now
    for x in list(animais):
        html += f"<h2> {x.name} - Pertence ao/à {x.dono.name} que tem {x.dono.idade} anos</h2>"

    html += "</body></html>"

    return HttpResponse(html)