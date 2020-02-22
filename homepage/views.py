# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

import csv

def homepage(request):
    return render(request, "homepage/homepage.html")

def upload(request):

	if request.method == "POST":
		uploaded_file = request.FILES["csv_file"]
		localFS = FileSystemStorage()
		localFS.save(uploaded_file.name, uploaded_file)

		data = uploaded_file.read().decode("UTF-8")

		print(data)

	return render(request, "homepage/upload.html", {"title" : "Upload Test"})
