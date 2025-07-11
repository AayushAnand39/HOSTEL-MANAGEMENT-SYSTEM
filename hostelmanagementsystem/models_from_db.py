# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HostelappAuthorities(models.Model):
    hallno = models.CharField(max_length=3, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)
    hallname = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phonenumber = models.CharField(max_length=11, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hostelapp_authorities'


class HostelappCheckincheckout(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_id = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hostelapp_checkincheckout'


class HostelappHalldetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    hall_no = models.IntegerField(blank=True, null=True)
    hall_name = models.CharField(max_length=100, blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hostelapp_halldetails'


class HostelappHostelcomplaints(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_id = models.CharField(max_length=50, blank=True, null=True)
    complaint = models.CharField(max_length=2500, blank=True, null=True)
    hall_no = models.IntegerField(blank=True, null=True)
    room_no = models.IntegerField(blank=True, null=True)
    addressed = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hostelapp_hostelcomplaints'


class HostelappMesscomplaints(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_id = models.CharField(max_length=50, blank=True, null=True)
    complaint = models.CharField(max_length=2500, blank=True, null=True)
    hall_no = models.IntegerField(blank=True, null=True)
    addressed = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hostelapp_messcomplaints'


class HostelappStudentpaymentdetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    student_name = models.CharField(max_length=100, blank=True, null=True)
    bank_account_no = models.CharField(max_length=50, blank=True, null=True)
    hostelpayment = models.IntegerField(blank=True, null=True)
    messpayment = models.IntegerField(blank=True, null=True)
    fine = models.IntegerField(blank=True, null=True)
    refund = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hostelapp_studentpaymentdetails'


class HostelappStudents(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_name = models.CharField(max_length=100, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    student_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    hall_no = models.IntegerField(blank=True, null=True)
    hall_name = models.CharField(max_length=100, blank=True, null=True)
    phonenumber = models.CharField(max_length=11, blank=True, null=True)
    phonenumber1 = models.CharField(max_length=11, blank=True, null=True)
    phonenumber2 = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    room_no = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hostelapp_students'
