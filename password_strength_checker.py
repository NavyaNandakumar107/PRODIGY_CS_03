# password strength checker
import re

# password must contain aleast 8 characters
password = input("Enter your password here: ")
if len(password) < 8:
    print("Password must contain atleast 8 characters")
# Password must contain atleast one uppercase letter
elif not re.search("[A-Z]", password):
    print("Password must contain atleast one uppercase letter.")
# Password must contain atleast one lowercase letter
elif not re.search("[a-z]", password):
    print("Password must contain atleast one lowercase letter.")
# Password must contain atleast one number
elif not re.search("[0-9]", password):
    print("Password must contain atleast one number.")
# Password must contain atleast one special character
elif not re.search("[!@#$%^&*()_+]", password):
    print("Password must contain atleast one special character.")    

else:
    print("Password is strong!")               
