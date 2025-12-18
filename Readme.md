# Secure Web Application Testing (SQLi & XSS)

This project is a simple Flask-based web application developed to understand
common web security vulnerabilities such as SQL Injection (SQLi) and
Cross-Site Scripting (XSS) in a controlled, self-built environment.

The project focuses on security-aware development, basic vulnerability
observation, and applying secure coding practices.

---

## Features
- Home page
- Login functionality
- Comment page
- Basic CSS styling
- SQLite database integration

---

## Security Concepts Covered
- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)
- Input validation
- Parameterized queries
- Output encoding

---

## Security Testing Performed

### SQL Injection
- Login functionality initially used insecure query handling
- Unexpected input caused incorrect application behavior
- Issue was fixed using parameterized SQL queries

### Cross-Site Scripting (XSS)
- User input was reflected without proper encoding
- Output encoding was applied to mitigate XSS risk

---

## Screenshots

### Normal Login
![Normal Login](screenshots/login_normal.png)

### SQL Injection Behavior (Before Fix)
![SQLi Before Fix](screenshots/login_unexpected_input.png)

### Login Secured (After Fix)
![Login Secured](screenshots/login_fixed.png)

### XSS Behavior (Before Fix)
![XSS Before Fix](screenshots/xss_before_fix.png)

### XSS Secured (After Fix)
![XSS Secured](screenshots/xss_after_fix.png)

---

## Tech Stack
- Python
- Flask
- SQLite
- HTML
- CSS

---

## Disclaimer
This project was created strictly for educational purposes.
All testing was performed on a self-developed application
in a controlled environment.
