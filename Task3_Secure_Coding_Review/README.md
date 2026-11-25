# Secure Coding Review

## 1. Project Overview
This project demonstrates secure password-handling practices using Python and reviews areas that can be improved.

## 2. Objective
To understand password hashing, random salt generation, password verification, and secure coding practices.

## 3. Technologies Used
- Bandit 1.9.4
- Python 3.14
- hashlib
- hmac
- os
- getpass

## 4. Security Features
- Password hashing using PBKDF2-HMAC-SHA256.
- Random salt generation.
- Password verification.
- Secure password comparison using hmac.compare_digest().
- Hidden password input using getpass.

## 5. Security Review
The program was reviewed for password-handling practices.

Areas identified for improvement:
- Persistent and secure password storage.
- Password length and strength validation.
- Login attempt limits.
- Username validation and account management.

## 6. Static Security Analysis
- Tool: Bandit 1.9.4
- Result: No issues identified.
- Total lines scanned: 35

## 7. Project Files
- secure_coding_review.py - Python demonstration.
- secure_coding_review_backup.py - Backup of original code.
- Security_Findings.md - Security review findings.
- Task3_Report.md - Project report.
- README.md - Project documentation.

## 8. How to Run
Open the terminal in this folder and run:

python secure_coding_review.py

## 9. Testing
The program was tested with a sample username and password. Password verification was successful.

## 10. Conclusion
This project demonstrates basic secure password-handling techniques and identifies improvements needed for a more secure login system.
