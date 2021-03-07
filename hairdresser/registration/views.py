from django.shortcuts import render

# Create your views here.


def hello(request):

    return render(request=request, template_name="registration/base.html", context={})

