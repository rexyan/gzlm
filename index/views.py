import json

from django.shortcuts import render, redirect, HttpResponse
from index import models


# Create your views here.

def index(request):
    all_lm = models.GZLM.objects.all()
    return render(
        request,
        'index.html',
        {"all_lm": all_lm}
    )


