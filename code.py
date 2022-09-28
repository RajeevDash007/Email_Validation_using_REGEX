import re

email_validation = "^[a-z]+[\.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

email_id = input("Enter your email address: ")
    

if re.search(email_validation, email_id):
    print("Valid Email ID")
else:
    print("Invalid Email ID")