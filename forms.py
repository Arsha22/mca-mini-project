from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import User
from .models import Room
from django import forms
from .models import Treatment,Package,Doctor
from django import forms
from .models import Booking,Room

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin',  'is_customer','is_staff',)


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['treatment_name', 'duration', 'cost', 'description','junior_doctor','senior_doctor']
class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['package_name', 'duration', 'cost', 'description']
#g

# app/forms.py



class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
