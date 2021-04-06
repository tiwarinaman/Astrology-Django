from django.contrib import messages
from django.shortcuts import render, redirect

from .models import UserDetails


# Create your views here.

def home(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', False)
        email = request.POST.get('email', False)
        mobile = request.POST.get('mobile_number', False)
        alt_number = request.POST.get('alternate_number', False)
        dob = request.POST.get('dob', False)
        time_of_birth = request.POST.get('time_of_birth', False)
        user_info = request.POST.get('user_info', False)
        password = request.POST.get('password', False)

        if full_name == '' or email == '' or mobile == '' or dob == '' or user_info == '' or password == '':
            messages.error(request, "All Fields are required !!!")
            redirect('home')
        else:
            try:
                user_details = UserDetails.objects.create(full_name=full_name, email=email, mobile=mobile,
                                                          dob=dob, user_info=user_info, password=password)

                if alt_number:
                    user_details.alternate_number = alt_number

                if time_of_birth:
                    user_details.time_of_birth = time_of_birth

                user_details.save()

                messages.success(request, "Your response has been recorded, we will contact you soon !!!")
                redirect('home')
            except Exception:
                messages.error(request, "Something Went Wrong")
                redirect('home')

    return render(request, 'home.html')
