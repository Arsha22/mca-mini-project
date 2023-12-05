from django.urls import path
from .import views
urlpatterns = [
        path('', views.home, name= 'home'),
        path('login/', views.login_view, name='login_view'),
        path('register/', views.register, name='register'),
        path('adminpage/', views.admin, name='adminpage'),
        path('customer/', views.customer, name='customer'),
        path('staff/', views.staff, name='staff'),
        path('addrooms/', views.add_room,name='add_rooms'),
        path('addstock/', views.addstock, name='addstock'),
        path('addpackage/', views.addpackage, name='addpackage'),
        path('addrooms/success/', views.success, name='success'),
        path('add_treatment/',views.add_treatment, name='add_treatment'),
        path('add_package/', views.add_package, name='add_package'),
        path('treatments/', views.treatment_list, name='treatment_list'),
        path('rooms/', views.rooms_list, name='rooms_list'),
        path('submit_booking/', views.submit_booking_view, name='submit_booking'),
        path('book/',views.book,name="book"),
        path('doctors/', views.DoctorListView.as_view(), name='doctor_list'),
        path('add_doctor/', views.add_doctor, name='add_doctor'),
        path('adbookings/',views.admin_booking_view, name='admin_bookings'),


]
