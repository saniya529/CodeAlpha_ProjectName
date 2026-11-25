# Secure Coding Review - Security Findings

## 1. Project Overview

This document reviews a Python password-handling program and identifies security strengths and areas for improvement.

## 2. Security Strengths

- PBKDF2-HMAC-SHA256 is used for password hashing.
- A random salt is generated for each password.
- hmac.compare_digest() is used for secure comparison.
- getpass hides password input.

## 3. Findings and Recommendations

### Finding 1: Password Storage

**Observation:** The program stores the salt and password hash only in memory.

**Recommendation:** Use secure database storage for persistent password records.

### Finding 2: Password Policy

**Observation:** The program does not check password length or strength.

**Recommendation:** Add password length and strength validation.

### Finding 3: Login Protection

**Observation:** The demo does not include login attempt limits.

**Recommendation:** Add rate limiting and temporary lockout in a real login system.

### Finding 4: User Management

**Observation:** The program does not check whether a username already exists.

**Recommendation:** Add proper username validation and account management.

## 4. Conclusion

The program demonstrates basic secure password-handling practices. Additional validation, protected storage, and login protection would improve its security.