#inputs password
password = input("enter password")
while (len(password))<8:
    print("password must be atleast  characters long")
    password = input("enter password")
print("password accepted")