from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

phone_no_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
)

class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False,null=True)
    is_customer = models.BooleanField('Is customer', default=False,null=True,)
    is_staff = models.BooleanField('Is employee', default=False,null=True)
    age=models.CharField(max_length=250,null=True,blank=True)
    city=models.CharField(max_length=25,null=True,blank=True)
    gender=models.CharField(max_length=250,blank=True,default="male")
    added_on=models.DateTimeField(auto_now_add=True,null=True)
    updated_on=models.DateTimeField(auto_now_add=True,null=True)


class Room(models.Model):
    roomid = models.AutoField(primary_key=True)
    roomno = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    room_image=models.ImageField(null=True,blank=True,upload_to="images/")

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # Add other fields for the doctor

    def __str__(self):
        return self.name

class Treatment(models.Model):
    treatment_id = models.AutoField(primary_key=True)
    treatment_name = models.CharField(max_length=255)
    duration = models.DurationField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    junior_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='junior_doctor')
    senior_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='senior_doctor')

    def __str__(self):
        return self.treatment_name

class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=255)
    duration = models.DurationField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def str(self):
        return self.package_name

# models.py
# models.py
class Booking(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255)
    appointment_date = models.DateField()
    # Add other fields as needed
    contact_number = models.CharField(max_length=15)  # Example additional field for contact number

class Booking(models.Model):
        treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
        room = models.ForeignKey(Room, on_delete=models.CASCADE)
        client_name = models.CharField(max_length=255)
        appointment_date = models.DateField()
        contact_number = models.CharField(max_length=15)

        def __str__(self):
            return f"{self.client_name}'s Booking for {self.treatment.treatment_name}"


