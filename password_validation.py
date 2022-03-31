import re
print("welcome to our website, please create an account")
username = input("enter a username:")
password = input("enter a password:")
display = '*'*len(password)
if len(password)<8:
    print("length of password must be more than 8")
elif " " in password:
    print("password shouls not contain any space")
elif not re.search('[0-9]',password):
    print("password should contin atleats one digit")
else:
    print("account created successfully")
    print("your username is:",username)
    print("your password is:",display)
