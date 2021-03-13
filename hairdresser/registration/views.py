from datetime import timedelta, datetime, date, time
from pytz import UTC as utc

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from .forms import SalonForm
from .models import Salon, Visit, Service
# Create your views here.

@login_required
def calendar_view(request, salon_id=None):
    """

    """

    if not salon_id:
        salon_id = 1

    try:
        salons = Salon.objects.get(id=salon_id)
    except ObjectDoesNotExist:
        raise Http404

    if request.method == "POST":
        form = SalonForm(request.POST)

        if form.is_valid():
            salon_pk = form.get_salon_pk()

            return HttpResponseRedirect(f'/registration/calendar/{salon_pk}')
    else:
        salon_pk = salon_id

    actual_date = date.today()
    actual_week_day = actual_date.weekday()
    date_from = actual_date - timedelta(days=actual_week_day)
    date_to = date_from + timedelta(days=actual_week_day-1)

    active_salon = Salon.objects.get(pk=salon_pk)
    time_open = active_salon.open_from
    time_close = active_salon.open_to

    # make data
    visits = Visit.objects.filter(pk=salon_pk)

    terms = [['free', 1]] * 44

    ctx = {
        'form': SalonForm(),
        'timeline': [],
        'date_from': date_from,
        'date_to': date_to,
        'timetable': {
            'monday': terms,
            'tuesday': terms,
            'wednesday': terms,
            'thursday': terms,
            'friday': terms},
    }

    def subtract_two_times(t1: time, t2: time) -> int:

        return (datetime.combine(date(1, 1, 1), t2) - datetime.combine(date(1, 1, 1), t1)).seconds // 60

    def inc_time(old_time, delta_hour=0, delta_minute=0):
        temp_date = datetime.combine(date(1, 1, 1), old_time) + timedelta(hours=delta_hour, minutes=delta_minute)
        return time(temp_date.hour, temp_date.minute)

    WEEK_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    pointed_date = date_from

    while pointed_date <= date_to:
        week_day = pointed_date.weekday()

        result = []
        visits = Visit.objects.filter(salon=salon_pk, start__gte=datetime.combine(pointed_date, time_open),
                                      start__lte=datetime.combine(pointed_date, time_close)).order_by('start')

        actual_hour = time_open
        i = 0
        while subtract_two_times(actual_hour, time_close) > 0:
            if i < len(visits):
                visit_start = visits[i].start
                visit_stop = visits[i].stop

                if subtract_two_times(actual_hour, time(visit_start.hour, visit_start.minute)) > 0:
                    delta_time = 15
                    result.append(['free', 20, actual_hour])
                else:
                    visit_length = subtract_two_times(time(visit_start.hour, visit_start.minute),
                                                      time(visit_stop.hour, visit_stop.minute))
                    result.append(['busy', visit_length + 5 * visit_length // 12, actual_hour])
                    i += 1
                    delta_time = subtract_two_times(time(visit_start.hour, visit_start.minute),
                                                    time(visit_stop.hour, visit_stop.minute))
            else:
                result.append(['free', 20, actual_hour])
                delta_time = 15

            actual_hour = inc_time(old_time=actual_hour, delta_minute=delta_time)

        ctx['timetable'].update({WEEK_DAYS[week_day]:result})
        pointed_date = pointed_date + timedelta(days=1)

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

