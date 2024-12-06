from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from datetime import datetime, timedelta



def home(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the data to the database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, "index.html")

    return render(request, "index.html")


def home_view(request):
    return render (request,"home.html")

from datetime import datetime, timedelta

def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        date = request.POST.get('date')  # Expected format: 'YYYY-MM-DD'
        time = request.POST.get('time')  # Expected format: 'HH:MM' or 'HH:MM:SS'
        am_pm = request.POST.get('ampm')  # AM or PM

        try:
            if len(time.split(':')) == 2:  # If time is in 'HH:MM' format
                time += ':00'  # Append seconds
            normalized_time = datetime.strptime(time, "%H:%M:%S").time()
        except ValueError as e:
            return JsonResponse({'success': False, 'message': f'Invalid time format: {e}'})

        try:
            appointment_datetime = datetime.strptime(f"{date} {normalized_time}", "%Y-%m-%d %H:%M:%S")
        except ValueError as e:
            return JsonResponse({'success': False, 'message': f'Invalid date or time format: {e}'})

        # Get existing appointments for the same date and am_pm
        existing_appointments = Appointment.objects.filter(date=date, am_pm=am_pm)

        for existing in existing_appointments:
            # Combine existing appointment's date and time into a datetime object
            existing_datetime = datetime.combine(
                existing.date,  # This is already a datetime.date object
                existing.time   # This is already a datetime.time object
            )

            time_difference = abs((appointment_datetime - existing_datetime).total_seconds())
            if time_difference < 30 * 60:  # 30 minutes in seconds
                return JsonResponse({'success': False, 'message': 'This slot conflicts with an existing appointment. Please choose a time at least 30 minutes apart.'})

        Appointment.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            date=date,
            time=normalized_time,
            am_pm=am_pm
        )

        # Respond with a JSON success message
        return JsonResponse({'success': True, 'message': 'Form submitted successfully!'})

    # Render the form for GET requests
    return render(request, 'appointment.html')

def gallery(request):
    return render(request,"gallery.html")