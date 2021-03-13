from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from .models import Salon, Visit, Service
# Create your views here.


# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             # log in the user
#             username = request.POST['username']
#             password = request.POST['password']
#             print(username, password)
#             user = authenticate(request, username=username, password=password)
#
#             print(f'{request.user} zalogowany')
#             if request.user.is_authenticated:
#                 print(f'{request.user} się zalogował')
#             return redirect('calendar')
#
#         else:
#             print('nic z tego')
#     else:
#         form = AuthenticationForm()
#
#     return render(request=request, template_name="registration/login.html", context={'form': form})


# def logout_view(request):
#     logout(request)


@login_required
def calendar_view(request):

    terms = [['free', 1]]*44
    print(terms)
    ctx = {
        'timeline': [],
        'timetable': {
            'monday': terms,
            'tuesday': terms,
            'wednesday': terms,
            'thursday': terms,
            'friday': terms},
    }

    return render(
        request=request,
        template_name='registration/calendar.html',
        context=ctx,
    )


def create_visit(request):

    return render(
        request=request,
        template_name='registration/create_visit.html',
        context={},
    )


@login_required
def salon_list(request):
    active_salons = Salon.objects.filter(active=True)
    inactive_salons = Salon.objects.filter(active=False)
    return render(request=request, template_name='registration/salon_list.html',
                  context={'active_salons': active_salons, 'inactive_salons': inactive_salons})


@login_required
def salon_detail(request, salon_id):
    employees = User.objects.filter(salon__id=salon_id)
    salon = get_object_or_404(Salon, id=salon_id)
    return render(request=request, template_name='registration/salon_detail.html',
                  context={'salon': salon, 'employees': employees})


@login_required
def visit_detail(request, visit_id):
    employee = User.objects.filter(visit__id=visit_id)
    visit = get_object_or_404(Visit, id=visit_id)
    service = Service.objects.get(name=visit.service)
    end_time = (visit.start + timedelta(minutes=service.service_length))
    final_price = service.price + visit.discount
    return render(request=request, template_name='registration/visit_detail.html',
                  context={'employee': employee, 'visit': visit, 'end_time': end_time, 'final_price': final_price})


@login_required
def user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request=request, template_name='registration/user_profile.html', context={'user': user})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully changed')
            return redirect('password_success')
        else:
            messages.error(request, "Ops...")
    else:
        form = PasswordChangeForm(request.user)
    return render(request=request, template_name='registration/change_password.html', context={'form': form})


@login_required
def password_success(request):
    return render(request=request, template_name='registration/password_success.html')


@login_required
def home_page(request):
    return render(request=request, template_name='registration/home_page.html')
