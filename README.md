# CodeAlpha_Secure-Coding-Review
This project illustrates a security audit on a small Python application
Secure Coding Audit — Python Application
📝 Description

This project illustrates a security audit on a small Python application using SQLite for user authentication.
It compares a vulnerable version (app.py) and a secure version (app_fixed.py) with:

Protection against SQL Injection

Secure password storage using bcrypt

Unit testing with pytest

Static analysis with Bandit

The goal is to demonstrate secure coding best practices and the process of detecting and fixing vulnerabilities.

📂 Project Structure
audit_task/
│
├─ app.py             # Vulnerable version
├─ app_fixed.py       # Fixed / secure version
├─ app_secure.py      # Example of secure code
├─ create_db.py       # SQLite database creation script
├─ users.db           # Test SQLite database
├─ test_auth.py       # Unit tests (pytest)
├─ bandit_before.txt  # Bandit report before fix
├─ bandit_after.txt   # Bandit report after fix
├─ pytest_output.txt  # Pytest results
└─ README.md          # This file

🚀 Prerequisites

Python 3.13 or higher

Python packages:

pip install bcrypt pytest bandit


SQLite (included with standard Python)

⚡ Installation & Usage

Clone the repository

git clone <https://github.com/manariwissal/CodeAlpha_Secure-Coding-Review>
cd audit_task


Create the database

python create_db.py


Add a test user (optional)

python -c "from app_fixed import create_user; create_user('testuser','TestPass123!')"


Test login

python -c "from app_fixed import check_login; print(check_login('testuser','TestPass123!'))"

🔒 Security Audit
1. Static analysis with Bandit

Before fix (app.py):

SQL Injection vulnerability detected (B608)

Risk: bypass authentication and modify data

After fix (app_fixed.py):

No issues detected

Parameterized queries and secure password hashing

2. Unit testing with pytest
pytest -q


3 tests passed: correct login, incorrect login, SQL injection attempt blocked

🛠 Applied Best Practices

Use parameterized queries (?) for SQL

Hash passwords with bcrypt

Properly close SQLite connections

Automated testing with pytest

Continuous security analysis with Bandit

📄 Key Commands
python -m bandit app.py > bandit_before.txt
python -m bandit app_fixed.py > bandit_after.txt
pytest -q > pytest_output.txt
python create_db.py

✅ Conclusion

The project demonstrates the identification and correction of an SQL Injection vulnerability.

After fixing, the code is secure and fully tested.

Recommended for learning secure coding best practices in Python.

📌 Author

Wissal Manari
Internship / Project: Secure Coding Review — Python
