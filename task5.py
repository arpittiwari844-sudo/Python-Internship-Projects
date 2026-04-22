import re

# Asking for User Password

password = input("Enter Your Password:") 

#Conditions

length_check = len(password) >=8
number_check = re.search(r"\d",password)
uppercase_check = re.search(r"[A-Z]",password)
special_check = re.search(r"[!@#$%^&*(),.\":{}|<>']",password)

#Checking Strength

if length_check and number_check and uppercase_check and special_check:
    print("Strong Password!")
else:
    print("Weak Password!")
    print("\nPassword Requirements:")

# Showing why it's weak

if not length_check:
    print("-Minimum 8 characters required")
if not uppercase_check:
    print("-Atleast one uppercase letter required")
if not number_check:
    print("-Atleast one number required")
if not special_check:
    print("-Atleast one special character required")