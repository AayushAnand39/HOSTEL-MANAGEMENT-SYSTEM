from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('authreg',views.authreg, name="authreg"),
    path('authlogin',views.authlogin, name="authlogin"),
    path('studreg',views.studreg, name="studreg"),
    path('studlogin',views.studlogin, name="studlogin"),
    path('authhome/<str:email>',views.authhome,name="authhome"),
    path('roomall/<str:email>',views.roomall,name="roomall"),
    path('studdetails/<str:email>', views.show_all_students, name='studdetails'),
    path("get-hall-name/", views.get_hall_name, name="get_hall_name"),
    path('hostelreg/<str:id>',views.hostelreg,name="hostelreg"),
    path('hostelcomp/<str:id>',views.hostel_complaint,name="hostel_comp"),
    path('messcomp/<str:id>',views.mess_complaint,name="mess_comp"),
    path('studprofile/<str:id>',views.studprofile,name="studprofile"),
    path('payhis/<str:id>',views.payhis,name="payhis"),
    path('studhome/<str:id>',views.studhome,name="studhome"),
    path('hall1/<str:email>',views.hall1_room_allotment,name="hall1"),
    path('hall2/<str:email>',views.hall2_room_allotment,name="hall2"),
    path('hall3/<str:email>',views.hall3_room_allotment,name="hall3"),
    path('hall4/<str:email>',views.hall4_room_allotment,name="hall4"),
    path('hall5/<str:email>',views.hall5_room_allotment,name="hall5"),
    path('hall6/<str:email>',views.hall6_room_allotment,name="hall6"),
    path('hostelcompview/<str:email>', views.hostel_comp_view, name='hostelcompview'),
    path('messcompview/<str:email>', views.mess_comp_view, name='messcompview'),
    path('authprofile/<str:email>',views.auth_profile, name='authprofile'),
    path('checkincheckout/<str:email>', views.checkincheckout_view, name='checkincheckout'),
    path('ajax/get-student-name/', views.get_student_name, name='get_student_name'),
    path('logout/<str:email>', views.auth_logout, name='auth_logout'),
    path('studlogout/<str:id>', views.stud_logout, name='stud_logout'),
]
