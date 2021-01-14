import json

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponse
from index import models
from BMS.settings import PAGE_SIZE


def index(request):
    all_lm = models.GZLM.objects.all()
    paginator = Paginator(all_lm, PAGE_SIZE)
    page = request.GET.get('page')
    lm = paginator.get_page(page)

    return render(
        request,
        'index.html',
        {"all_lm": lm}
    )


