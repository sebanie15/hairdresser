from datetime import timedelta

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Salon, Visit, Service
# Create your views here.


def hello(request):
    return render(request=request, template_name="registration/base.html", context={})


def salon_list(request):
    active_salons = Salon.objects.filter(active=True)
    inactive_salons = Salon.objects.filter(active=False)
    return render(request=request, template_name='registration/salon_list.html',
                  context={'active_salons': active_salons, 'inactive_salons': inactive_salons})


def salon_detail(request, salon_id):
    employees = User.objects.filter(salon__id=salon_id)
    salon = get_object_or_404(Salon, id=salon_id)
    return render(request=request, template_name='registration/salon_detail.html',
                  context={'salon': salon, 'employees': employees})


def visit_detail(request, visit_id):
    employee = User.objects.filter(visit__id=visit_id)
    visit = get_object_or_404(Visit, id=visit_id)
    service = Service.objects.get(name=visit.service)
    end_time = (visit.start + timedelta(minutes=service.service_length))
    final_price = service.price + visit.discount
    return render(request=request, template_name='registration/visit_detail.html',
                  context={'employee': employee, 'visit': visit, 'end_time': end_time, 'final_price': final_price})
