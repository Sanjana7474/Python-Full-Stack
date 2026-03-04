name=input("Enter the name: ")
dob= input("Enter the dob[YYYY-MM-DD]: ")
username=name[:2]+name[-2]+dob[-2:]+dob[2:4]
print(f"Hi {name} !\nYour Username: {username}")
