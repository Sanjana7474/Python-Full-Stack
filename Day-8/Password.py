password=input("Enter the password:")
if len(password)>=8:
    s=set()
    for i in password:
        if i.isupper():
            s.add("upper")
        elif i.islower():
            s.add("lower")
        elif i.isdigit():
            s.add("digits")
        else:
            s.add("Special Characters")
    if len(s)==4:
        print("Strong Password")
    else:
        print("Weak Password. Password needs to have Upper Case, Lower Case, Digits and Special Characters")
else:
    print(" length needs to be >=8")
