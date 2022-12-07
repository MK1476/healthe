from django.shortcuts import render
from doctor.models import Doctor
from department.models import Department
from . models import Appointment
from datetime import datetime, timedelta
from django.utils import timezone
import pytz
from . forms import AppointmentForm
from patient.models import Patient
from staff.models import Staff
from django.conf import settings

# Create your views here.
def create(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            apt = form.save(commit=False)
            if request.user.is_staff:
                staff = Staff.objects.get(user=request.user)
                apt.issued_staff = staff

                pat_id = form.data['pat_id']
                patient = Patient.objects.get(pk=pat_id)
                apt.patient = patient
            else:
                patient = Patient.objects.filter(user=request.user)[0]
                apt.patient = patient

            date, time = form.data['date'], form.data['slots']
            print(date, time)
            dt = timezone.make_aware(datetime.strptime(f'{date} {time}', '%Y-%m-%d %H:%M'), pytz.timezone(settings.TIME_ZONE))
            apt.date_time_of_appointment = dt
            form.save()

    departments = Department.objects.all()
    doctors = Doctor.objects.none()
    return render(request, 'appointment/forms.html', {'departments': departments, 'doctors': doctors})


def load_doctors(request):
    department_id = request.GET.get('department_id')
    doctors = Doctor.objects.filter(department_id=department_id)
    print(doctors)
    return render(request, 'appointment/render_doctors.html', {'doctors': doctors})

def time_slots(request):
    print('working')
    doctor_id = request.GET.get('doctor_id')
    date = request.GET.get('date')
    
    appointments = Appointment.objects.filter(doctor_id=doctor_id)
    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except:
        return render(request, 'appointment/render_slots.html', {'slots': []})

    start, stop = doctor.working_hours.split('-')
    start_dt, stop_dt = [timezone.make_aware(datetime.strptime(f'{date} {limit}', '%Y-%m-%d %H:%M'), pytz.timezone(settings.TIME_ZONE)) for limit in [start,stop]]
    
    current_range = start_dt
    interval = timedelta(minutes=30)
    slots = [current_range]

    if stop_dt.hour == 0:
        stop_dt += timedelta(days=1)
    
    if appointments:
        if date:
            t_apts = [timezone.localtime(appointment.date_time_of_appointment) for appointment in appointments]
            while start_dt <= current_range < stop_dt:
                current_range += interval
                if current_range in t_apts:
                    continue
                slots.append(current_range)
    else:
        if date:
            while start_dt <= current_range < stop_dt:
                current_range += interval
                slots.append(current_range)
            
    slots = list(map(lambda dt: datetime.strftime(dt, '%H:%M'), slots))

    return render(request, 'appointment/render_slots.html', {'slots': slots})
