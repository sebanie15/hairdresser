from django.shortcuts import render, get_object_or_404
from .models import Salon
# Create your views here.


def hello(request):

    return render(request=request, template_name="registration/base.html", context={})


def salon_list(request):
    active_salons = Salon.objects.filter(active=True)
    inactive_salons = Salon.objects.filter(active=False)
    return render(request=request, template_name='registration/salon_list.html',
                  context={'active_salons': active_salons, 'inactive_salons': inactive_salons})


def salon_detail(request, salon_id):
    salon = get_object_or_404(Salon, id=salon_id)
    return render(request=request, template_name='registration/salon_detail.html', context={'salon': salon})
