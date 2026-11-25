Task 3 - Secure Coding Review

1. Introduction
This project demonstrates secure password handling using Python and reviews basic security practices.

2. Objective
To understand password hashing, random salt generation, password verification, and secure coding improvements.

3. Tools Used
- Python 3.14
- hashlib
- hmac
- os
- getpass

4. Implementation
The program uses PBKDF2-HMAC-SHA256 to generate a password hash with a random salt.

It also uses hmac.compare_digest() for secure password comparison and getpass to hide password input.

5. Security Strengths
- Secure password hashing.
- Random salt generation.
- Secure password comparison.
- Hidden password input.

6. Security Findings
The code review identified the following areas for improvement:

- Password records are stored only in memory.
- Password length and strength validation are not implemented.
- Login attempt limits are not implemented.
- Username and account management features are not included.

7. Recommendations
- Use secure persistent storage for password records.
- Add password validation.
- Implement login attempt limits.
- Add proper username and account management.

8. Testing
The program was tested with a sample username and password. Password verification was successful.

9. Static Security Analysis
Tool Used: Bandit 1.9.4

The Python source code was scanned using Bandit.
Result: No issues identified.

Total lines scanned: 35
Total security issues detected: 0.

10. Conclusion
The project demonstrates basic secure password-handling practices and identifies areas that can be improved to make a login system more secure.