from django.shortcuts import render
from django.http import HttpResponse, request
from django.utils.translation import get_language


def index(request):
    lg = get_language()
    context = {'lg': lg}
    return render(request, 'index.html', context)
