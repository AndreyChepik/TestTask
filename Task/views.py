from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import ClassifierModel
from .forms import CodeForm
from django.views.generic import View

class Foo(View):
    def get(self, request):
        form = CodeForm
        return render(request, 'Task/main.html', context={'form': form})
   # nums = ClassifierModel.objects.all()

