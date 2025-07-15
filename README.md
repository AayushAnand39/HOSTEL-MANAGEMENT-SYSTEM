# HOSTEL-MANAGEMENT-SYSTEM

## VIDEO DEMO OF THE HOSTEL MANAGEMENT SYSTEM
<a href="https://drive.google.com/file/d/1OyRp1rQcrcoCezkwzqI3alShi1uxCBC5/view?usp=sharing">Click to view the video demo of the Hostel Management System</a>


## TABLE STRUCTURE

### 📊 Table: `hostelapp_authorities`

| Field        | Type          | Null | Key | Default | Description                     |
|--------------|---------------|------|-----|---------|---------------------------------|
| `hallno`     | `varchar(3)`  | YES  |     | `NULL`  | Hall number of the authority    |
| `password`   | `varchar(100)`| YES  |     | `NULL`  | Password               |
| `email`      | `varchar(100)`| NO   |     | `NULL`  | Email ID (used as unique login)|
| `hallname`   | `varchar(100)`| YES  |     | `NULL`  | Full name of the hall           |
| `name`       | `varchar(100)`| YES  |     | `NULL`  | Full name of the authority      |
| `phonenumber`| `varchar(11)` | YES  |     | `NULL`  | Contact number                  |
| `position`   | `varchar(100)`| YES  |     | `NULL`  | Position (e.g., Warden)         |
| `isLoggedIn` | `varchar(3)`  | NO   |     | `NO`    | Login status: 'YES' or 'NO'     |

### 📊 Table: `hostelapp_checkincheckout`

| Field        | Type          | Null | Key | Default | Extra           | Description                                  |
|--------------|---------------|------|-----|---------|------------------|----------------------------------------------|
| `id`         | `bigint`      | NO   | PRI | NULL    | `auto_increment` | Unique identifier for each record            |
| `student_id` | `varchar(50)` | YES  |     | NULL    |                  | Student ID (foreign key reference optional)  |
| `name`       | `varchar(100)`| YES  |     | NULL    |                  | Full name of the student                     |
| `check_in`   | `datetime(6)` | YES  |     | NULL    |                  | Timestamp of student check-in                |
| `check_out`  | `datetime(6)` | YES  |     | NULL    |                  | Timestamp of student check-out               |

### 📊 Table: `hostelapp_halldetails`

| Field       | Type           | Null | Key | Default | Extra           | Description                             |
|-------------|----------------|------|-----|---------|------------------|-----------------------------------------|
| `id`        | `bigint`       | NO   | PRI | NULL    | `auto_increment` | Unique identifier for the record        |
| `hall_no`   | `int`          | YES  |     | NULL    |                  | Numeric code for the hall               |
| `hall_name` | `varchar(100)` | YES  |     | NULL    |                  | Name of the hall                        |
| `degree`    | `varchar(100)` | YES  |     | NULL    |                  | Degree (e.g., B.Tech, M.Tech, Ph.D.)    |
| `year`      | `int`          | YES  |     | NULL    |                  | Year of study (e.g., 1, 2, 3, 4)         |
| `gender`    | `varchar(8)`   | YES  |     | NULL    |                  | Gender category (e.g., Male, Female)    |

### 📊 Table: `hostelapp_hostelcomplaints`

| Field        | Type            | Null | Key | Default | Extra           | Description                               |
|--------------|------------------|------|-----|---------|------------------|-------------------------------------------|
| `student_id` | `varchar(50)`    | YES  |     | NULL    |                  | ID of the student raising the complaint   |
| `complaint`  | `varchar(2500)`  | YES  |     | NULL    |                  | Detailed description of the complaint     |
| `hall_no`    | `int`            | YES  |     | NULL    |                  | Hall number where the issue occurred      |
| `room_no`    | `int`            | YES  |     | NULL    |                  | Room number involved in the complaint     |
| `addressed`  | `varchar(4)`     | YES  |     | NULL    |                  | Status flag: e.g., 'YES' or 'NO'          |
| `id`         | `int`            | NO   | PRI | NULL    | `auto_increment` | Unique complaint ID                       |

### 📊 Table: `hostelapp_messcomplaints`

| Field        | Type            | Null | Key | Default | Extra           | Description                                 |
|--------------|------------------|------|-----|---------|------------------|---------------------------------------------|
| `student_id` | `varchar(50)`    | YES  |     | NULL    |                  | ID of the student submitting the complaint  |
| `complaint`  | `varchar(2500)`  | YES  |     | NULL    |                  | Description of the mess-related complaint   |
| `hall_no`    | `int`            | YES  |     | NULL    |                  | Hall number to which the mess belongs       |
| `addressed`  | `varchar(4)`     | YES  |     | NULL    |                  | Status of complaint: 'YES' or 'NO'          |
| `id`         | `int`            | NO   | PRI | NULL    | `auto_increment` | Unique complaint ID                         |

## 📊 Table: `hostelapp_studentpaymentdetails`

| Field            | Type           | Null | Key | Default | Description                                        |
|------------------|----------------|------|-----|---------|----------------------------------------------------|
| `student_id`     | `varchar(50)`  | YES  |     | NULL    | Unique ID of the student                          |
| `student_name`   | `varchar(100)` | YES  |     | NULL    | Full name of the student                          |
| `bank_account_no`| `varchar(50)`  | YES  |     | NULL    | Bank account number for refunds                   |
| `hostelpayment`  | `int`          | YES  |     | NULL    | Amount paid for hostel accommodation              |
| `messpayment`    | `int`          | YES  |     | NULL    | Amount paid for mess services                     |
| `fine`           | `int`          | YES  |     | NULL    | Total fines levied on the student                 |
| `refund`         | `int`          | YES  |     | NULL    | Refund amount processed or to be processed        |

### 📊 Table: `hostelapp_students`

| Field           | Type           | Null | Key | Default | Extra           | Description                                    |
|------------------|----------------|------|-----|---------|------------------|------------------------------------------------|
| `id`             | `bigint`       | NO   | PRI | NULL    | `auto_increment` | Internal unique ID                             |
| `student_name`   | `varchar(100)` | YES  |     | NULL    |                  | Full name of the student                       |
| `father_name`    | `varchar(100)` | YES  |     | NULL    |                  | Father's name                                  |
| `mother_name`    | `varchar(100)` | YES  |     | NULL    |                  | Mother's name                                  |
| `degree`         | `varchar(100)` | YES  |     | NULL    |                  | Degree program (e.g., B.Tech, M.Tech)          |
| `student_id`     | `varchar(50)`  | YES  | UNI | NULL    |                  | Unique student identifier (e.g., Roll No.)     |
| `year`           | `int`          | YES  |     | NULL    |                  | Year of study                                   |
| `hall_no`        | `int`          | YES  |     | NULL    |                  | Hall number assigned                            |
| `hall_name`      | `varchar(100)` | YES  |     | NULL    |                  | Hall name                                       |
| `phonenumber`    | `varchar(11)`  | YES  |     | NULL    |                  | Primary phone number                            |
| `phonenumber1`   | `varchar(11)`  | YES  |     | NULL    |                  | Alternate phone number 1                        |
| `phonenumber2`   | `varchar(11)`  | YES  |     | NULL    |                  | Alternate phone number 2                        |
| `email`          | `varchar(100)` | YES  |     | NULL    |                  | Email address                                   |
| `password`       | `varchar(100)` | YES  |     | NULL    |                  | Password          |
| `room_no`        | `int`          | YES  |     | NULL    |                  | Allotted room number                            |
| `gender`         | `varchar(6)`   | YES  |     | NULL    |                  | Gender (e.g., Male, Female, Other)             |
| `isLoggedIn`     | `varchar(3)`   | NO   |     | NO      |                  | Login status (`YES` or `NO`)                   |

---



