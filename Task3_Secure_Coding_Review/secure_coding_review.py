# TASK 3: SECURE CODING REVIEW

import hashlib
import os
import hmac
import getpass

def hash_password(password):
    salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        200000
    )

    return salt, password_hash


def verify_password(password, salt, stored_hash):
    new_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        200000
    )

    return hmac.compare_digest(new_hash, stored_hash)


print("SECURE LOGIN DEMO")

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

salt, stored_hash = hash_password(password)

print("\nPassword processed securely.")
print("Username:", username)

check_password = getpass.getpass(
    "Re-enter password to verify: "
)

if verify_password(check_password, salt, stored_hash):
    print("Password verification successful.")
else:
    print("Password verification failed.")

print("\nSECURITY REVIEW COMPLETE")