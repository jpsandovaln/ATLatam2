from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse

from .exception.compiler_exception import CompilerException
from .model.compiler_facade import CompilerFacade
from django.core.files.storage import FileSystemStorage


class Compiler(View):

    def post(self, request):
        try:
            upload_file = request.FILES['file']
            fs = FileSystemStorage()
            fs.save(upload_file.name, upload_file)
            language = request.POST['language']
            version = request.POST['version']
            result = CompilerFacade.compile(language, 'D:/code/EjemploJava8.java', 'D:/code/ ',
                                            'C:/"Program Files"/Java/jdk1.8.0_251/bin/')
            return HttpResponse(result, "application/json")
        except CompilerException as error:
            return HttpResponse(error, status=error.status)
        except Exception as error:
            return HttpResponse(error, status="500")
