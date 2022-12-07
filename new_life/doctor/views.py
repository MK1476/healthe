from django.shortcuts import render
from . forms import DoctorForm
from . models import Doctor
from department.models import Department
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse

from new_life.constants import BLOOD_GROUPS, WORKING_HOURS, GENDER_CHOICES

# Create your views here.
def create(request):
    form = DoctorForm()
    error = ""
    
    print(request.method)
    
    departments = Department.objects.all()
    if request.method == 'POST':
        data = request.POST.copy()
        form = DoctorForm(data, request.FILES)
        print(form.files)
        username = data['user_name']
        pw, rep_pw = data['password'], data['repeat_password']
        if pw == rep_pw:
            user, not_created = User.objects.get_or_create(username=username)
            if form.is_valid():
                if not_created:
                    user.set_password(pw)
                
                    doctor = form.save(commit=False)
                    doctor.user = user

                    doctor.save()
                    user.save()
                else:
                    error = 'User already exists'

            else:
                error = form.errors
        else:
            error = "Make sure to enter the same password"

    return render(request, 'doctor/forms.html', {'form': form, 'genders': GENDER_CHOICES, 'departments': departments, 'blood_groups': BLOOD_GROUPS, 'working_hours': WORKING_HOURS, "error": error})

# class DoctorView(FormView):
#     template_name = 'forms.html'
#     form_class = DoctorForm
#     success_url = reverse_lazy('doctor:new')

#     def get_context_data(self, val='', **kwargs):
#         print('executing context')
#         departments = Department.objects.all()
#         context = super().get_context_data() | {'genders': GENDER_CHOICES, 'departments': departments, 'blood_groups': BLOOD_GROUPS, 'working_hours': WORKING_HOURS, 'error': val}
#         print(context)
#         return context

#     # def form_valid(self, form):
#     #     data = form.cleaned_data
#     #     print(data)
#     #     username = data['user_name']
#     #     pw, rep_pw = data['password'], data['repeat_password'] 
#     #     if pw == rep_pw:
#     #         user, not_created = User.objects.get_or_create(username=username)
#     #         if not_created:
#     #             user.set_password(pw)
            
#     #             doctor = form.save(commit=False)
#     #             doctor.user = user

#     #             doctor.save()
#     #             user.save()
#     #         else:
#     #             self.errors = 'User already exists'

#     #     else:
#     #         self.errors = "Make sure to enter the same password"

#     #     if self.errors:
#     #         print(self.errors)
#     #         print(self.get_context_data(self.errors))
#     #         self.success_url = reverse('doctor:create')
        
#     #     return super().form_valid(form)

#     def form_invalid(self, form):
#         self.errors = form.errors
#         print(self.get_context_data())
        
#         return super().form_invalid(form)

#     def post(self, request, *args, **kwargs):
#         form = DoctorForm(request.POST, request.FILES)
#         data = form.data
#         print(data)
#         username = data['user_name']
#         pw, rep_pw = data['password'], data['repeat_password'] 
#         if pw == rep_pw:
#             user, not_created = User.objects.get_or_create(username=username)
#             if form.is_valid():
#                 if not_created:
#                     user.set_password(pw)
                
#                     doctor = form.save(commit=False)
#                     doctor.user = user

#                     doctor.save()
#                     user.save()
#                 else:
#                     self.errors = 'User already exists'
#             else:
#                 self.errors = form.errors
#         else:
#             self.errors = "Make sure to enter the same password"

#         if self.errors:
#             print(self.errors)
#             print(self.get_context_data(self.errors))
#             self.success_url = reverse('doctor:create')
#         return super().post(request, *args, **kwargs)
    
def home(request):
    return render(request, 'index.html', {'name': 'Nihaal'})