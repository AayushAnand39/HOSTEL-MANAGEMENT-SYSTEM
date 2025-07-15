# HOSTEL-MANAGEMENT-SYSTEM

## Video Demo of the Hostel Management System
<a href="https://drive.google.com/file/d/1OyRp1rQcrcoCezkwzqI3alShi1uxCBC5/view?usp=sharing">Click to view the video demo of the Hostel Management System</a>


## TABLE STRUCTURE

### 📊 Table: `Authorities`

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

---
