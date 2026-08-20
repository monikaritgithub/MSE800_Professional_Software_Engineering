# SQLite University Database Activity

A lightweight Python application demonstrating SQLite database creation, schema modeling with foreign key constraints, mock data seeding, and relational SQL queries using `sqlite3`.

---

## 📁 Project Structure

```text
activity_4_sqlite3-university-db/
│
├── schema.sql       # Database structure and table definitions (DDL)
├── seed.sql         # Initial mock data insertion statements (DML)
├── main.py          # Primary Python execution script
├── queries.sql      # Standalone reference SQL queries
└── university.db    # Auto-generated SQLite database file (created on runtime)
```

---

## 🗄️ Database Schema

The database models a university domain and includes the following tables:

* **`student`**: Stores student personal details (`NID`, `F_NAME`, `L_NAME`, `B_DATE`, `ADDRESS`, `EMAIL_ADDRESS`).
* **`SUBJECTS`**: Details academic subjects (`SUBJECT_CODE`, `SUBJECT_UNIT`, `SUBJECT_UCFS`).
* **`LECTURER`**: Stores teaching staff profiles (`L_ID`, `L_LASTNAME`, `L_FIRSTNAME`, `L_EMAIL`, `L_ADDRESS`).
* **`ENROLLMENT`**: Junction table mapping student subject registrations with foreign keys (`STUDENT_NUM`, `SUBJECT_CODE`).
* **`Lecture`**: Captures scheduled lecture sessions linked to subjects and lecturers (`CCA`, `Subject_Code`, `Lecturer_ID`, `Date`, `Time`).

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.x** installed on your system.
* No external pip packages required (`sqlite3` is built into the Python standard library).

### Execution

1. Open your terminal or PowerShell prompt in the project directory:
   ```bash
   cd activity_4_sqlite3-university-db
   ```

2. *(Optional)* If you need to perform a complete reset of the database, delete any existing `.db` file:
   ```powershell
   Remove-Item university.db -ErrorAction Ignore
   ```

3. Run the main execution script:
   ```bash
   python main.py
   ```

---

## 📊 Sample Output

Running `main.py` executes `schema.sql` and `seed.sql`, then outputs the analytical query results directly to the console:

```text
Setting up database schema...
Seeding initial data...

=========================================
Q1: Registered Students Count Per Subject
=========================================
Subject Code: 101             | Enrolled: 2
Subject Code: 102             | Enrolled: 1
Subject Code: 103             | Enrolled: 0

=========================================
Q2: Students Enrolled in >1 Subject
=========================================
ID: 1001 | Name: Moni Smith          | Total Subjects: 2
```

---

## 🛠️ Troubleshooting

* **`sqlite3.OperationalError: near "EXITS": syntax error`**: Ensure `schema.sql` uses `IF NOT EXISTS` (with an **S**).
* **`sqlite3.IntegrityError: UNIQUE constraint failed`**: Occurs if duplicate records are inserted. Delete `university.db` before re-running `main.py` to ensure a clean build.