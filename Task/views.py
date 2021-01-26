from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import ClassifierModel
from .forms import CodeForm
from django.views.generic import View
from django.shortcuts import redirect


class Foo(View):
    def get(self, request):
        """returns form page, where the user can input values"""
        form = CodeForm
        return render(request, 'Task/main.html', context={'form': form})

    def post(self, request):
        bound_form = CodeForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            res = ClassifierModel.objects.all()
            return render(request, 'Task/success.html', context={'form' : res})
        return render(request, 'Task/alert.html', context={'form' : bound_form})


