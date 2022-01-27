from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse
import json
from .model.compiler_facade import CompilerFacade
from django.core.files.storage import FileSystemStorage


class Compiler(View):

    def post(self, request):
        print('******123')
        upload_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(upload_file.name, upload_file)
        language = request.POST['language']
        version = request.POST['version']

        result = CompilerFacade.compile('java', 'D:/code/EjemploJava8.java', 'D:/code/ ',
                               'C:/"Program Files"/Java/jdk1.8.0_251/bin/')
        return HttpResponse(result, "application/json")
