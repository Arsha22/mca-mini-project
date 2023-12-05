from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Treatment,Doctor
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Room
from django.shortcuts import render, redirect
from .models import Treatment
from .forms import TreatmentForm,PackageForm,DoctorForm
from django.views.generic import ListView
from .models import Room
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Treatment, Booking

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Treatment, Booking
# Create your views here.


from django.urls import reverse

def home(request):
    return render(request,'home.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_staff:
                login(request, user)
                return redirect('staff')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def customer(request):
    return render(request,'customer.html')


def staff(request):
    return render(request,'employee.html')

def addtreatment(request):
    return render(request,'adminsection/add_treatment.html')
def addstock(request):
    return render(request,'adminsection/medicalstock.html')
def addpackage(request):
    return render(request,'adminsection/addpackage.html')


def add_room(request):
    if request.method == 'POST':
        room_number = request.POST.get('roomNumber')
        room_type = request.POST.get('roomType')
        capacity = request.POST.get('capacity')
        price = request.POST.get('price')

        # Handle image upload
        room_image = request.FILES.get('roomImage')
        fs = FileSystemStorage()
        filename = fs.save(room_image.name, room_image)

        # Create a new Room object and save it
        Room.objects.create(
            roomno=room_number,
            type=room_type,
            capacity=capacity,
            price=price,
            room_image=filename  # Save the filename in the 'room_image' field
        )

        # Redirect to a room list view or any other page
        return redirect('success')

    return render(request, 'adminsection/add_room.html')


def success(request):
    return render(request,'admin.html')


#treatment
  # You need to create a form for your model fields

def add_treatment(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success_page' with the URL you want to redirect to upon successful submission
    else:
        form = TreatmentForm()

    return render(request, 'adminsection/add_treatment.html', {'form': form})

def add_package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success_page' with the URL you want to redirect to upon successful submission
    else:
        form = PackageForm()

    return render(request, 'adminsection/addpackage.html', {'form': form})

#treatmentdisplay
# views.py

# views.py

def treatment_list(request):
    treatments = Treatment.objects.all()
    return render(request, 'customersection/treatment_list.html', {'treatments': treatments})

def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, 'customersection/room_list.html', {'rooms': rooms})

# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Booking, Treatment, Room

def submit_booking_view(request):
    if request.method == 'POST':
        # Get the form data
        treatment_id = request.POST.get('treatment')
        roomid = request.POST.get('room')
        client_name = request.POST.get('client_name')
        appointment_date = request.POST.get('appointment_date')
        contact_number = request.POST.get('contact_number')

        # Fetch Treatment and Room objects based on the selected IDs
        treatment = Treatment.objects.get(pk=treatment_id)
        room = Room.objects.get(pk=roomid)

        # Create a new Booking instance
        booking = Booking(
            treatment=treatment,
            room=room,
            client_name=client_name,
            appointment_date=appointment_date,
            contact_number=contact_number
        )

        # Save the booking to the database
        booking.save()

        # You can add a success message or redirect to another page
        return HttpResponse("Booking submitted successfully!")

    else:
        # Handle GET requests or other cases as needed
        return HttpResponse("Invalid request method.")

def book(request):
    treatments = Treatment.objects.all()
    rooms = Room.objects.all()
    return render(request, 'customersection/book_treatment.html', {'treatments': treatments, 'rooms': rooms})
# app/views.py
 # Create a DoctorForm in forms.py

class DoctorListView(View):
    template_name = 'adminsection/doctor_list.html'

    def get(self, request, *args, **kwargs):
        doctors = Doctor.objects.all()
        return render(request, self.template_name, {'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()

    return render(request, 'adminsection/add_doctor.html', {'form': form})

# views.py


def admin_booking_view(request):
    bookings = Booking.objects.all()
    return render(request, 'adminsection/admin_booking.html', {'bookings': bookings})

