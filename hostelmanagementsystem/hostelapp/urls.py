from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('authreg',views.authreg, name="authreg"),
    path('authlogin',views.authlogin, name="authlogin"),
    path('studreg',views.studreg, name="studreg"),
    path('studlogin',views.studlogin, name="studlogin"),
    path('authhome',views.authhome,name="authhome"),
    path('roomall',views.roomall,name="roomall"),
    path('studdetails', views.show_all_students, name='studdetails'),
    path("get-hall-name/", views.get_hall_name, name="get_hall_name"),
    path('hostelreg',views.hostelreg,name="hostelreg"),
    path('hostelcomp',views.hostel_complaint,name="hostel_comp"),
    path('messcomp',views.mess_complaint,name="mess_comp"),
    path('studprofile',views.studprofile,name="studprofile"),
    path('payhis',views.payhis,name="payhis"),
    path('studhome',views.studhome,name="studhome"),
    path('hall1',views.hall1_room_allotment,name="hall1"),
    path('hall2',views.hall2_room_allotment,name="hall2"),
    path('hall3',views.hall3_room_allotment,name="hall3"),
    path('hall4',views.hall4_room_allotment,name="hall4"),
    path('hall5',views.hall5_room_allotment,name="hall5"),
    path('hall6',views.hall6_room_allotment,name="hall6"),
    path('hostelcompview', views.hostel_comp_view, name='hostelcompview'),
    path('messcompview', views.mess_comp_view, name='messcompview'),
    path('authprofile',views.auth_profile, name='authprofile'),
    path('checkincheckout/', views.checkincheckout_view, name='checkincheckout'),
    path('ajax/get-student-name/', views.get_student_name, name='get_student_name'),
    path('logout/', views.auth_logout, name='auth_logout'),
    path('studlogout/', views.stud_logout, name='stud_logout'),
]
