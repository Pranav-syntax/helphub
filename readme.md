🎓 Student Course Registration System
A sophisticated, full-stack web application designed for educational institutions to manage student enrollments, course catalogs, and faculty assignments. Built with Python Flask and MySQL, featuring a modern, professional Lavender-themed UI.

🚀 Features
For Students
Secure Authentication: Professional login and registration system with unique username validation.

Smart Dashboard: View all currently enrolled courses and assigned faculty at a glance.

Course Discovery: Searchable database of available courses with real-time filtering.

One-Click Enrollment: Simplified registration for new academic programs.

For Administrators
Master Control Panel: Centralized hub for managing the entire campus database.

Student Management: View, update student details (including password resets), or remove records.

Faculty Management: Add new faculty members with automatic ID generation and department tracking.

Course Management: Create and edit courses, linking them to specific faculty members.

Live Analytics: Real-time tracking of enrollment numbers per course.

🛠️ Tech Stack
Backend: Python 3.x, Flask

Database: MySQL

Frontend: HTML5, CSS3 (Modern Glassmorphism & Lavender UI), JavaScript (ES6)

Authentication: Flask Session Management

📂 Project Structure
Plaintext
├── app.py              # Main Flask application & SQL logic
├── templates/          # UI Components
│   ├── auth.html       # Student Login & Registration
│   ├── dashboard.html  # Student Personal Console
│   ├── admin_login.html# Secure Admin Entry
│   └── admin.html      # Administrative Master Panel
└── static/             # (Optional) CSS and Images
⚙️ Installation & Setup
Clone the Repository

Bash
git clone https://github.com/your-username/tist-portal.git
cd tist-portal
Install Dependencies

Bash
pip install flask mysql-connector-python
Database Configuration
Create a MySQL database named reged and run the following schema:

SQL
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    name VARCHAR(100),
    age INT,
    password VARCHAR(255)
);

CREATE TABLE Faculty (
    faculty_id INT AUTO_INCREMENT PRIMARY KEY,
    faculty_name VARCHAR(100),
    department VARCHAR(100)
);

CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100),
    duration VARCHAR(50),
    faculty_id INT,
    FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id)
);

CREATE TABLE Enrollments (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
Run the Application

Bash
python app.py
Access the portal at http://127.0.0.1:5000

🔐 Admin Credentials
Username: admin123

Password: tist

Developed for Academic Project. Feel free to star ⭐ this repository if you find it helpful!
