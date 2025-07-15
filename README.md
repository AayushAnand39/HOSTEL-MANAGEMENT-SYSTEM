# HOSTEL-MANAGEMENT-SYSTEM

## Video Demo of the Hostel Management System
<a href="https://drive.google.com/file/d/1OyRp1rQcrcoCezkwzqI3alShi1uxCBC5/view?usp=sharing">Click to view the video demo of the Hostel Management System</a>


## TABLE STRUCTURE

### 📊 Table: `hostelapp_authorities`

| Field        | Type          | Null | Key | Default | Description                     |
|--------------|---------------|------|-----|---------|---------------------------------|
| `hallno`     | `varchar(3)`  | YES  |     | `NULL`  | Hall number of the authority    |
| `password`   | `varchar(100)`| YES  |     | `NULL`  | Password (hashed)               |
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


