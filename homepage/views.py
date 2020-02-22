# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, "homepage/homepage.html")

def upload(request):
	return render(request, "homepage/upload.html", {"title" : "Upload Test"})
