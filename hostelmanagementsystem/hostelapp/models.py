from django.db import models

# Create your models here.
class Authorities(models.Model):
    email = models.CharField(max_length=100, primary_key=True, default="example@email.com")
    name = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    hallno = models.CharField(max_length=3, null=True)
    hallname = models.CharField(max_length=100, null=True)
    phonenumber = models.CharField(max_length=11, null=True)
    password = models.CharField(max_length=100, null=True)
    isLoggedIn = models.CharField(max_length=3, null=True, default="NO")


class Students(models.Model):
    student_id = models.CharField(max_length=50, primary_key=True, default="00000000")
    student_name = models.CharField(max_length=100, null=True)
    father_name = models.CharField(max_length=100, null=True)
    mother_name = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=6, null=True)
    year = models.IntegerField(null=True)
    hall_no = models.IntegerField(null=True)
    hall_name = models.CharField(max_length=100, null=True)
    phonenumber = models.CharField(max_length=11, null=True)
    phonenumber1 = models.CharField(max_length=11, null=True)
    phonenumber2 = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    room_no = models.IntegerField(null=True)
    isLoggedIn = models.CharField(max_length=3, null=True, default="NO")
    
class StudentPaymentDetails(models.Model):
    payment_id = models.CharField(max_length=50, primary_key=True, default="00000000")
    student_id = models.CharField(max_length=50, null=True)
    student_name = models.CharField(max_length=100, null=True)
    bank_account_no = models.CharField(max_length=50, null=True)
    hostelpayment = models.IntegerField(null=True)
    messpayment = models.IntegerField(null=True)
    fine = models.IntegerField(null=True)
    refund = models.IntegerField(null=True)

class HallDetails(models.Model):
    hall_no = models.IntegerField(null=True)
    hall_name = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)
    gender = models.CharField(max_length=8, null=True)


class HostelComplaints(models.Model):
    student_id = models.CharField(max_length=50, null=True, unique=True)
    complaint = models.CharField(max_length=2500, null=True)
    hall_no = models.IntegerField(null=True)
    room_no = models.IntegerField(null=True)
    addressed = models.CharField(max_length=4, null=True)

class MessComplaints(models.Model):
    student_id = models.CharField(max_length=50, null=True, unique=True)
    complaint = models.CharField(max_length=2500, null=True)
    hall_no = models.IntegerField(null=True)
    addressed = models.CharField(max_length=4, null=True)

class CheckInCheckOut(models.Model):
    student_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100, null=True)
    check_in = models.DateTimeField(null=True)
    check_out = models.DateTimeField(null=True)