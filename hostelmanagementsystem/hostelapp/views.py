from django.shortcuts import render, redirect
from django.db import connection
from .models import HallDetails
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def authreg(request):
    if request.method == "POST":
        name = request.POST.get("name")
        position = request.POST.get("position")
        hallno = request.POST.get("hallno")
        hallname = request.POST.get("hallname")
        phonenumber = request.POST.get("phonenumber")
        email = request.POST.get("email")
        password1 = request.POST.get("setpassword")
        password2 = request.POST.get("checkpassword")
        if password1 != password2:
            print("Passwords do not match")
            return render(request, "authreg.html", {"error": "Passwords do not match"})
        else:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO hostelapp_authorities (name, position, hallno, hallname, phonenumber, email, password)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, [name, position, hallno, hallname, phonenumber, email, password1])
            return render(request, "authreg.html", {"success": "Registration successful!"})
    return render(request, "authreg.html")

        
def authlogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        # Query the database only on email and password.
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM hostelapp_authorities 
                WHERE email = %s AND password = %s
            """, [email, password])
            user = cursor.fetchone()

        if user:
            # Use the retrieved id from the database record.
            # auth_id = user[0]
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE hostelapp_authorities
                    SET isLoggedIn = 'YES'
                    WHERE email = %s
                """,[email])
            print("Login successful, email:", email)
            # request.session['auth_id'] = auth_id  # Setting session variable
            return redirect(authhome, email=email)
        else:
            print("Invalid login details")
            return render(request, "authlogin.html", {"error": "Invalid login credentials"})
    else:
        return render(request, "authlogin.html")

def authhome(request, email):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_authorities
            WHERE email = %s    
        """,[email])
        user = cursor.fetchone()
    if user[7] == "YES":
        return render(request,"authhome.html",{"email": email})
    else :
        return render(request, "authlogin.html", {"error": "Not Logged In"})

def studreg(request):
    if request.method == "POST":
        student_name = request.POST.get("name")
        father_name = request.POST.get("name1")
        mother_name = request.POST.get("name2")
        degree = request.POST.get("degree")
        student_id = request.POST.get("id")
        gender = request.POST.get("gender")
        year = request.POST.get("year")
        student_phone_number = request.POST.get("phonenumber")
        student_phone_number1 = request.POST.get("phonenumber1")
        student_phone_number2 = request.POST.get("phonenumber2")
        email = request.POST.get("email")
        password1 = request.POST.get("setpassword")
        password2 = request.POST.get("checkpassword")
        if password1!=password2:
            print("Passwords do not match")
            return render(request, "authreg.html", {"error": "Passwords do not match"})
        else:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO hostelapp_students (student_name, father_name, mother_name, degree, gender, student_id, year, phonenumber, phonenumber1, phonenumber2, email, password)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, [student_name, father_name, mother_name, degree, gender, student_id, year, student_phone_number, student_phone_number1, student_phone_number2, email, password1])
            return render(request, "studreg.html", {"success": "Registration successful!"})
    else:
        return render(request,"studreg.html")
    
def studlogin(request):
    if request.method == "POST":
        student_id = request.POST.get("id")
        email = request.POST.get("email")
        password = request.POST.get("password")
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * from hostelapp_students 
                WHERE student_id = %s AND email = %s AND password = %s
            """,[student_id,email,password])
            user = cursor.fetchone()
            if user:
                print("Login successful")
                print("student id: " + student_id + " email: " + email)
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE hostelapp_students
                        SET isLoggedIn = 'YES'
                        WHERE student_id = %s AND email = %s AND password = %s
                    """,[student_id, email, password])
                return redirect('studhome',id=student_id)  
                # return authhome(request)
            else:
                print("Some issues with details")
                return render(request,"studlogin.html",{"error":"Invalid login credentials"})
    else:
        return render(request,"studlogin.html",{"error":"Invalid login credentials"})

def roomall(request, email):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_authorities
            WHERE email = %s    
        """,[email])
        user = cursor.fetchone()
    if user[7] == "YES":
        return render(request,"roomall.html",{"email":email})
    else :
        return render(request, "authlogin.html", {"error": "Not Logged In"})

def studhome(request,id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_students
            WHERE student_id = %s;
        """,[id])
        user = cursor.fetchone()
    if (not user) or user[16] == "NO":
        return render(request,"studlogin.html",{"error":"Invalid login credentials"})
    else:
        return render(request,"studhome.html",{"id":id})

def get_hall_name(request):
    hallno = request.GET.get("hallno")
    with connection.cursor() as cursor:
        cursor.execute("SELECT hall_name FROM hostelapp_halldetails WHERE hall_no = %s", [hallno])
        row = cursor.fetchone()
    return JsonResponse({"hall_name": row[0] if row else None})


def hostelreg(request, id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_students
            WHERE student_id = %s;
        """,[id])
        user = cursor.fetchone()
    if (not user) or user[16] == "NO":
        return render(request,"studlogin.html",{"error":"Invalid login credentials"})

    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * 
                FROM hostelapp_students 
                WHERE student_id = %s
            """, [id])
            columns = [col[0] for col in cursor.description]
            row = cursor.fetchone()
        
        if row:
            data = dict(zip(columns, row))
            name = data['student_name']
            year = data['year']
            email = data['email']
            phonenumber = data['phonenumber']
            room_no = data['room_no']
            return render(request, "hostelreg.html", {
                "student_id": id,
                "name": name,
                "year": year,
                "email": email,
                "phonenumber": phonenumber,
                "room_no": room_no
            })
        else:
            return render(request, "hostelreg.html", {"error": "Student not found"})

    elif request.method == "POST":
        # Get fixed fields
        name = request.POST.get("name")
        student_id = request.POST.get("student_id")
        year = request.POST.get("year")
        email = request.POST.get("email")
        phonenumber = request.POST.get("phonenumber")
        room_no = request.POST.get("room_no")

        # Editable fields
        hallno = request.POST.get("hallno")
        bankaccountno = request.POST.get("bankaccountno")
        seatrent = request.POST.get("seatrent")
        messfees = request.POST.get("messfees")

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO hostelapp_studentpaymentdetails 
                (student_id, student_name, bank_account_no, hostelpayment, messpayment, fine, refund)
                VALUES (%s, %s, %s, %s, %s, 0, 0)
                ON DUPLICATE KEY UPDATE
                    bank_account_no = VALUES(bank_account_no),
                    hostelpayment = VALUES(hostelpayment),
                    messpayment = VALUES(messpayment)
            """, [student_id, name, bankaccountno, seatrent, messfees])

        return render(request, "hostelreg.html", {
            "student_id": id,
            "name": name,
            "year": year,
            "email": email,
            "phonenumber": phonenumber,
            "room_no": room_no,
            "success": "Payment details saved successfully."
        })

def payhis(request, id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_students
            WHERE student_id = %s;
        """,[id])
        user = cursor.fetchone()
    if (not user) or user[16] == "NO":
        return render(request,"studlogin.html",{"error":"Invalid login credentials"})

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT student_id, student_name, bank_account_no, hostelpayment, messpayment, fine, refund
            FROM hostelapp_studentpaymentdetails
            WHERE student_id = %s
        """, [id])
        payment_data = cursor.fetchall()

    return render(request, "payhis.html", {"payments": payment_data, "id":id})

def hostel_complaint(request,id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_students
            WHERE student_id = %s;
        """,[id])
        user = cursor.fetchone()
    if (not user) or user[16] == "NO":
        return render(request,"studlogin.html",{"error":"Invalid login credentials"})
    
    if request.method == 'POST':
        degree = request.POST.get('degree')
        gender = request.POST.get('gender')
        year = request.POST.get('year')
        complaint = request.POST.get('complaint')

        # Step 1: Retrieve the student details based on degree, gender, and year
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT student_id, hall_no, room_no
                FROM hostelapp_students
                WHERE student_id = %s, degree = %s AND gender = %s AND year = %s
            """, [id,degree, gender, year])

            student = cursor.fetchone()  # Get the first result if exists
            
            if student:
                student_id, hall_no, room_no = student

                # Step 2: Insert the complaint into the HostelComplaints table
                cursor.execute("""
                    INSERT INTO hostelapp_hostelcomplaints (student_id, complaint, hall_no, room_no, addressed)
                    VALUES (%s, %s, %s, %s, %s)
                """, [student_id, complaint, hall_no, room_no, 'No'])

                # Step 3: Return success response
                return HttpResponse("Complaint submitted successfully.")
            else:
                # Step 4: If no student is found, return failure message
                return HttpResponse("No student found matching the criteria.")
    
    return render(request, 'hostelcomp.html',{"id":id})

def mess_complaint(request,id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_students
            WHERE student_id = %s;
        """,[id])
        user = cursor.fetchone()
    if (not user) or user[16] == "NO":
        return render(request,"studlogin.html",{"error":"Invalid login credentials"})
    hall_no = None

    if id:
        with connection.cursor() as cursor:
            cursor.execute("SELECT hall_no FROM hostelapp_students WHERE student_id = %s", [id])
            row = cursor.fetchone()
            if row:
                hall_no = row[0]

    if request.method == 'POST':
        complaint = request.POST.get('complaint')
        addressed = 'No'

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO hostelapp_messcomplaints (student_id, complaint, hall_no, addressed)
                VALUES (%s, %s, %s, %s)
            """, [id, complaint, hall_no, addressed])

        return redirect('messcomp',id=id)

    return render(request, 'messcomp.html', {
        'student_id': id,
        'hall_no': hall_no
    })

def studprofile(request,id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_students
            WHERE student_id = %s;
        """,[id])
        user = cursor.fetchone()
    if (not user) or user[16] == "NO":
        return render(request,"studlogin.html",{"error":"Invalid login credentials"})

    context = {}

    with connection.cursor() as cursor:
        # Fetch student profile info
        cursor.execute("""
            SELECT student_name, father_name, mother_name, degree, gender, year, 
                   hall_no, hall_name, room_no, phonenumber, phonenumber1, 
                   phonenumber2, email, student_id
            FROM hostelapp_students
            WHERE student_id = %s
        """, [id])
        student_data = cursor.fetchone()

        if student_data:
            context.update({
                'student_name': student_data[0],
                'father_name': student_data[1],
                'mother_name': student_data[2],
                'degree': student_data[3],
                'gender': student_data[4],
                'year': student_data[5],
                'hall_no': student_data[6],
                'hall_name': student_data[7],
                'room_no': student_data[8],
                'phonenumber': student_data[9],
                'phonenumber1': student_data[10],
                'phonenumber2': student_data[11],
                'email': student_data[12],
                'student_id': id,
            })

        # Fetch hostel complaints
        cursor.execute("""
            SELECT complaint, hall_no, room_no, addressed
            FROM hostelapp_hostelcomplaints
            WHERE student_id = %s
        """, [id])
        context['hostel_complaints'] = cursor.fetchall()

        # Fetch mess complaints
        cursor.execute("""
            SELECT complaint, hall_no, addressed
            FROM hostelapp_messcomplaints
            WHERE student_id = %s
        """, [id])
        context['mess_complaints'] = cursor.fetchall()

    return render(request, 'studprofile.html', context)

def show_all_students(request, email):
    # Get 'hall' from query params; default to 'all'
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_authorities
            WHERE email = %s    
        """,[email])
        user = cursor.fetchone()
    if (not user) or (user[7] == 'NO'):
        return render(request,"authlogin.html",{"error":"User not found or not logged in"})
    hall = request.GET.get('hall', 'all')

    with connection.cursor() as cursor:
        if hall == 'all':
            cursor.execute("""
                SELECT student_name, father_name, mother_name, degree, gender,
                       student_id, year, hall_no, hall_name, phonenumber,
                       phonenumber1, phonenumber2, email, room_no
                FROM hostelapp_students
            """)
        else:
            cursor.execute("""
                SELECT student_name, father_name, mother_name, degree, gender,
                       student_id, year, hall_no, hall_name, phonenumber,
                       phonenumber1, phonenumber2, email, room_no
                FROM hostelapp_students
                WHERE hall_no = %s
            """, [hall])

        student_list = cursor.fetchall()

    return render(request, 'studdetails.html', {
        'students': student_list,
        'hall': hall,
        'email' : email
    })


def hall1_room_allotment(request, email):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_authorities
            WHERE email = %s    
        """,[email])
        user = cursor.fetchone()
    if (not user) or (user[7] == 'NO'):
        return render(request,"authlogin.html",{"error":"User not found or not logged in"})
    
    hall_no = 1

    # 1️⃣ Fetch the hall name
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT hall_name FROM hostelapp_halldetails WHERE hall_no = %s",
            [hall_no]
        )
        row = cursor.fetchone()
    hall_name = row[0] if row else "Unknown Hall"

    # 2️⃣ Pull *all* students already in this hall, then group by room
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT student_id, room_no "
            "FROM hostelapp_students "
            "WHERE hall_no = %s",
            [hall_no]
        )
        assigned = cursor.fetchall()  # list of (student_id, room_no)

    room_members = {}
    for student_id, room_no in assigned:
        room_members.setdefault(room_no, []).append(student_id)

    # 3️⃣ Build the rooms list, with occupancy and member‑lists
    rooms = []
    total_rooms = 10
    for rn in range(1, total_rooms + 1):
        members   = room_members.get(rn, [])
        occupancy = len(members)
        rooms.append({
            'room_no':  rn,
            'members':  members,
            'occupancy': occupancy
        })

    # 4️⃣ Handle new allotment
    if request.method == 'POST':
        student_id = request.POST['student_id'].strip()
        room_no    = int(request.POST['room_no'])

        # re‑check occupancy
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) "
                "FROM hostelapp_students "
                "WHERE hall_no = %s AND room_no = %s",
                [hall_no, room_no]
            )
            current_occupancy = cursor.fetchone()[0]

            if current_occupancy >= 3:
                messages.error(request, f"Room {room_no} is already full.")
            else:
                # do the update in the *same* table
                cursor.execute(
                    "UPDATE hostelapp_students "
                    "SET hall_no = %s, hall_name = %s, room_no = %s "
                    "WHERE student_id = %s",
                    [hall_no, hall_name, room_no, student_id]
                )
                messages.success(
                    request,
                    f"Student {student_id} allotted to Room {room_no}."
                )

        # Redirect back so that we re‑compute occupancy & members
        return redirect('hall1',email=email)

    return render(request, 'hall1.html', {
        'hall_no':   hall_no,
        'hall_name': hall_name,
        'rooms':     rooms,
        'email' :    email
    })

def hall2_room_allotment(request, email):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_authorities
            WHERE email = %s    
        """,[email])
        user = cursor.fetchone()
    if (not user) or (user[7] == 'NO'):
        return render(request,"authlogin.html",{"error":"User not found or not logged in"})
    hall_no = 2

    # 1️⃣ Fetch the hall name from HallDetails
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT hall_name FROM hostelapp_halldetails WHERE hall_no = %s",
            [hall_no]
        )
        row = cursor.fetchone()
    hall_name = row[0] if row else "Unknown Hall"

    # 2️⃣ Fetch all students already assigned to this hall
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT student_id, room_no "
            "FROM hostelapp_students "
            "WHERE hall_no = %s",
            [hall_no]
        )
        assigned = cursor.fetchall()  # list of (student_id, room_no)

    # Group by room_no
    room_members = {}
    for student_id, room_no in assigned:
        room_members.setdefault(room_no, []).append(student_id)

    # 3️⃣ Build rooms list (1–10)
    rooms = []
    total_rooms = 10
    for rn in range(1, total_rooms + 1):
        members   = room_members.get(rn, [])
        occupancy = len(members)
        rooms.append({
            'room_no':   rn,
            'members':   members,
            'occupancy': occupancy
        })

    # 4️⃣ Handle allotment POST
    if request.method == 'POST':
        student_id = request.POST['student_id'].strip()
        room_no    = int(request.POST['room_no'])

        # re‑check occupancy
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) "
                "FROM hostelapp_students "
                "WHERE hall_no = %s AND room_no = %s",
                [hall_no, room_no]
            )
            current_occupancy = cursor.fetchone()[0]

            if current_occupancy >= 3:
                messages.error(request, f"Room {room_no} is already full.")
            else:
                cursor.execute(
                    "UPDATE hostelapp_students "
                    "SET hall_no = %s, hall_name = %s, room_no = %s "
                    "WHERE student_id = %s",
                    [hall_no, hall_name, room_no, student_id]
                )
                messages.success(
                    request,
                    f"Student {student_id} allotted to Room {room_no} in Hall {hall_no}."
                )

        return redirect('hall2',email=email)

    return render(request, 'hall2.html', {
        'hall_no':   hall_no,
        'hall_name': hall_name,
        'rooms':     rooms,
        'email' :    email
    })
 
def hall3_room_allotment(request, email):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_authorities
            WHERE email = %s    
        """,[email])
        user = cursor.fetchone()
    if (not user) or (user[7] == 'NO'):
        return render(request,"authlogin.html",{"error":"User not found or not logged in"})
    hall_no = 3

    # 1️⃣ Get hall_name from HallDetails
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT hall_name FROM hostelapp_halldetails WHERE hall_no = %s",
            [hall_no]
        )
        row = cursor.fetchone()
    hall_name = row[0] if row else "Unknown Hall"

    # 2️⃣ Fetch all students already assigned to this hall
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT student_id, room_no "
            "FROM hostelapp_students "
            "WHERE hall_no = %s",
            [hall_no]
        )
        assigned = cursor.fetchall()  # [(student_id, room_no), ...]

    # Group students by room_no
    room_members = {}
    for student_id, room_no in assigned:
        room_members.setdefault(room_no, []).append(student_id)

    # 3️⃣ Build room list for rooms 1–10
    rooms = []
    total_rooms = 10
    for rn in range(1, total_rooms + 1):
        members   = room_members.get(rn, [])
        occupancy = len(members)
        rooms.append({
            'room_no':   rn,
            'members':   members,
            'occupancy': occupancy
        })

    # 4️⃣ Handle new allotment POST
    if request.method == 'POST':
        student_id = request.POST['student_id'].strip()
        room_no    = int(request.POST['room_no'])

        # Re‑check occupancy
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) FROM hostelapp_students WHERE hall_no = %s AND room_no = %s",
                [hall_no, room_no]
            )
            current_occupancy = cursor.fetchone()[0]

            if current_occupancy >= 3:
                messages.error(request, f"Room {room_no} is already full.")
            else:
                cursor.execute(
                    "UPDATE hostelapp_students "
                    "SET hall_no = %s, hall_name = %s, room_no = %s "
                    "WHERE student_id = %s",
                    [hall_no, hall_name, room_no, student_id]
                )
                messages.success(
                    request,
                    f"Student {student_id} allotted to Room {room_no} in Hall {hall_no}."
                )

        return redirect('hall3',email=email)

    return render(request, 'hall3.html', {
        'hall_no':   hall_no,
        'hall_name': hall_name,
        'rooms':     rooms,
        'email' :    email
    })
 
def hall4_room_allotment(request, email):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_authorities
            WHERE email = %s    
        """,[email])
        user = cursor.fetchone()
    if (not user) or (user[7] == 'NO'):
        return render(request,"authlogin.html",{"error":"User not found or not logged in"})
    hall_no = 4

    # 1️⃣ Fetch hall_name
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT hall_name FROM hostelapp_halldetails WHERE hall_no = %s",
            [hall_no]
        )
        row = cursor.fetchone()
    hall_name = row[0] if row else "Unknown Hall"

    # 2️⃣ Fetch all students already assigned to this hall
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT student_id, room_no "
            "FROM hostelapp_students "
            "WHERE hall_no = %s",
            [hall_no]
        )
        assigned = cursor.fetchall()  # [(student_id, room_no), ...]

    # Group students by room_no
    room_members = {}
    for student_id, room_no in assigned:
        room_members.setdefault(room_no, []).append(student_id)

    # 3️⃣ Build rooms list (rooms 1–10)
    rooms = []
    total_rooms = 10
    for rn in range(1, total_rooms + 1):
        members   = room_members.get(rn, [])
        occupancy = len(members)
        rooms.append({
            'room_no':   rn,
            'members':   members,
            'occupancy': occupancy
        })

    # 4️⃣ Handle new allotment POST
    if request.method == 'POST':
        student_id = request.POST['student_id'].strip()
        room_no    = int(request.POST['room_no'])

        # Re‑check occupancy
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) FROM hostelapp_students WHERE hall_no = %s AND room_no = %s",
                [hall_no, room_no]
            )
            current_occupancy = cursor.fetchone()[0]

            if current_occupancy >= 3:
                messages.error(request, f"Room {room_no} is already full.")
            else:
                cursor.execute(
                    "UPDATE hostelapp_students "
                    "SET hall_no = %s, hall_name = %s, room_no = %s "
                    "WHERE student_id = %s",
                    [hall_no, hall_name, room_no, student_id]
                )
                messages.success(
                    request,
                    f"Student {student_id} allotted to Room {room_no} in Hall {hall_no}."
                )

        return redirect('hall4',email=email)

    return render(request, 'hall4.html', {
        'hall_no':   hall_no,
        'hall_name': hall_name,
        'rooms':     rooms,
        'email' :    email
    })
 
def hall5_room_allotment(request, email):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_authorities
            WHERE email = %s    
        """,[email])
        user = cursor.fetchone()
    if (not user) or (user[7] == 'NO'):
        return render(request,"authlogin.html",{"error":"User not found or not logged in"})
    hall_no = 5

    # 1️⃣ Fetch hall_name
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT hall_name FROM hostelapp_halldetails WHERE hall_no = %s",
            [hall_no]
        )
        row = cursor.fetchone()
    hall_name = row[0] if row else "Unknown Hall"

    # 2️⃣ Fetch all students already assigned to this hall
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT student_id, room_no "
            "FROM hostelapp_students "
            "WHERE hall_no = %s",
            [hall_no]
        )
        assigned = cursor.fetchall()  # [(student_id, room_no), ...]

    # Group students by room_no
    room_members = {}
    for student_id, room_no in assigned:
        room_members.setdefault(room_no, []).append(student_id)

    # 3️⃣ Build rooms list (rooms 1–10)
    rooms = []
    total_rooms = 10
    for rn in range(1, total_rooms + 1):
        members   = room_members.get(rn, [])
        occupancy = len(members)
        rooms.append({
            'room_no':   rn,
            'members':   members,
            'occupancy': occupancy
        })

    # 4️⃣ Handle new allotment POST
    if request.method == 'POST':
        student_id = request.POST['student_id'].strip()
        room_no    = int(request.POST['room_no'])

        # Re‑check occupancy
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) FROM hostelapp_students WHERE hall_no = %s AND room_no = %s",
                [hall_no, room_no]
            )
            current_occupancy = cursor.fetchone()[0]

            if current_occupancy >= 3:
                messages.error(request, f"Room {room_no} is already full.")
            else:
                cursor.execute(
                    "UPDATE hostelapp_students "
                    "SET hall_no = %s, hall_name = %s, room_no = %s "
                    "WHERE student_id = %s",
                    [hall_no, hall_name, room_no, student_id]
                )
                messages.success(
                    request,
                    f"Student {student_id} allotted to Room {room_no} in Hall {hall_no}."
                )

        return redirect('hall5',email=email)

    return render(request, 'hall5.html', {
        'hall_no':   hall_no,
        'hall_name': hall_name,
        'rooms':     rooms,
        'email' :    email
    })
 
def hall6_room_allotment(request, email):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_authorities
            WHERE email = %s    
        """,[email])
        user = cursor.fetchone()
    if (not user) or (user[7] == 'NO'):
        return render(request,"authlogin.html",{"error":"User not found or not logged in"})
    hall_no = 6

    # 1️⃣ Fetch hall_name
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT hall_name FROM hostelapp_halldetails WHERE hall_no = %s",
            [hall_no]
        )
        row = cursor.fetchone()
    hall_name = row[0] if row else "Unknown Hall"

    # 2️⃣ Fetch all students already assigned to this hall
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT student_id, room_no "
            "FROM hostelapp_students "
            "WHERE hall_no = %s",
            [hall_no]
        )
        assigned = cursor.fetchall()  # [(student_id, room_no), ...]

    # Group students by room_no
    room_members = {}
    for student_id, room_no in assigned:
        room_members.setdefault(room_no, []).append(student_id)

    # 3️⃣ Build rooms list (rooms 1–10)
    rooms = []
    total_rooms = 10
    for rn in range(1, total_rooms + 1):
        members   = room_members.get(rn, [])
        occupancy = len(members)
        rooms.append({
            'room_no':   rn,
            'members':   members,
            'occupancy': occupancy
        })

    # 4️⃣ Handle new allotment POST
    if request.method == 'POST':
        student_id = request.POST['student_id'].strip()
        room_no    = int(request.POST['room_no'])

        # Re‑check occupancy
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) FROM hostelapp_students WHERE hall_no = %s AND room_no = %s",
                [hall_no, room_no]
            )
            current_occupancy = cursor.fetchone()[0]

            if current_occupancy >= 3:
                messages.error(request, f"Room {room_no} is already full.")
            else:
                cursor.execute(
                    "UPDATE hostelapp_students "
                    "SET hall_no = %s, hall_name = %s, room_no = %s "
                    "WHERE student_id = %s",
                    [hall_no, hall_name, room_no, student_id]
                )
                messages.success(
                    request,
                    f"Student {student_id} allotted to Room {room_no} in Hall {hall_no}."
                )

        return redirect('hall6',email=email)

    return render(request, 'hall6.html', {
        'hall_no':   hall_no,
        'hall_name': hall_name,
        'rooms':     rooms,
        'email' :    email
    })

def hostel_comp_view(request, email):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_authorities
            WHERE email = %s    
        """,[email])
        user = cursor.fetchone()
    if (not user) or (user[7] == 'NO'):
        return render(request,"authlogin.html",{"error":"User not found or not logged in"})
    # Handle “mark addressed” action
    if request.method == 'POST':
        comp_id = request.POST.get('comp_id')
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE hostelapp_hostelcomplaints "
                "SET addressed = 'Yes' "
                "WHERE id = %s",
                [comp_id]
            )
        messages.success(request, "Complaint marked as addressed.")
        return redirect('hostelcompview',email=email)

    # Fetch all un‑addressed complaints
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, student_id, complaint, hall_no, room_no
            FROM hostelapp_hostelcomplaints
            WHERE addressed = 'No'
        """)
        complaints = cursor.fetchall()  # [(id, student_id, complaint, hall_no, room_no), ...]

    return render(request, 'hostelcompview.html', {
        'complaints': complaints,
        'email' : email
    })

def mess_comp_view(request, email):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_authorities
            WHERE email = %s    
        """,[email])
        user = cursor.fetchone()
    if (not user) or (user[7] == 'NO'):
        return render(request,"authlogin.html",{"error":"User not found or not logged in"})
    # 1️⃣ Handle “mark addressed” POST
    if request.method == 'POST':
        comp_id = request.POST.get('comp_id')
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE hostelapp_messcomplaints "
                "SET addressed = 'Yes' "
                "WHERE id = %s",
                [comp_id]
            )
        messages.success(request, "Mess complaint marked as addressed.")
        return redirect('messcompview',email=email)

    # 2️⃣ Fetch all un‑addressed mess complaints
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, student_id, complaint, hall_no
            FROM hostelapp_messcomplaints
            WHERE addressed = 'No'
        """)
        complaints = cursor.fetchall()  # [(id, student_id, complaint, hall_no), ...]

    return render(request, 'messcompview.html', {
        'complaints': complaints,
        "email" : email
    })

def auth_profile(request, email):
    # Check if 'auth_id' exists in the session
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_authorities
            WHERE email = %s
        """,[email])
        user = cursor.fetchone()
    if (not user) or user[7] == "NO":
        # If no valid session, redirect to login page
        return redirect('/authlogin')

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM hostelapp_authorities
            WHERE email = %s
        """, [email])
        row = cursor.fetchone()

    if row:
        context = {
            'name': row[4],
            'position': row[6],
            'hallno': row[0],
            'hallname': row[3],
            'phonenumber': row[5],
            'email': row[2]
        }
    else:
        # Handle case where the id does not match a record.
        context = {"error": "No profile data found."}

    return render(request, "authprofile.html", context)

def checkincheckout_view(request, email):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM hostelapp_authorities
            WHERE email = %s    
        """,[email])
        user = cursor.fetchone()
    if (not user) or (user[7] == 'NO'):
        return render(request,"authlogin.html",{"error":"User not found or not logged in"})
    
    if request.method == 'POST':
        sid      = request.POST['student_id']
        name     = request.POST['name']
        check_in = request.POST['check_in']
        check_out= request.POST['check_out'] or None

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO hostelapp_checkincheckout
                (student_id, name, check_in, check_out)
                VALUES (%s, %s, %s, %s)
            """, [sid, name, check_in, check_out])

        return redirect('checkincheckout', email=email)

    # GET → fetch all existing entries
    with connection.cursor() as cursor:
        cursor.execute("""
          SELECT student_id, name, check_in, check_out
          FROM hostelapp_checkincheckout
          ORDER BY check_in DESC
        """)
        rows = cursor.fetchall()
    entries = [
      {'student_id': r[0], 'name': r[1], 'check_in': r[2], 'check_out': r[3]}
      for r in rows
    ]
    return render(request, 'checkincheckout.html', {'entries': entries, 'email' : email})


@require_GET
def get_student_name(request):
    sid = request.GET.get('student_id')
    name = ''
    with connection.cursor() as cursor:
        cursor.execute("""
          SELECT name
          FROM hostelapp_students
          WHERE student_id = %s
        """, [sid])
        row = cursor.fetchone()
        if row:
            name = row[0]
    return JsonResponse({'name': name})


def auth_logout(request, email):
    # clear all session data
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE hostelapp_authorities
            SET isLoggedIn = 'NO'
            WHERE email = %s
        """,[email])
    # optional: show a one‑time message
    messages.info(request, "You have been logged out.")
    return redirect('authlogin')

def stud_logout(request,id):
    # clear session completely
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE hostelapp_students
            SET isLoggedIn = 'NO'
            WHERE student_id = %s
        """,[id])
    return redirect('studlogin')