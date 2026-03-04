s=int(input("Enter the how many students:"))
names=[]
gpa=[]
max_val=0
max_name=''
min_val=10
min_name=''
for i in range(s):
    print(f"-----------Student-{i+1}-----------")
    name=input("Enter the name: ")
    cgpa=float(input("Enter the gpa: "))
    if cgpa>max_val:
        max_name=name
        max_val=cgpa
    if cgpa<min_val:
        min_name=name
        min_val=cgpa
        
    names.append(name)
    gpa.append(cgpa)
print('f{"Names".ljust(15)} {"GPA".ljust(5)}')
print('-'*20)
for i in range(len(names)):
    print(f'{names[i].ljust(14)}| {str(gpa[i]).ljust(5)}')
print(f"Highest GPA-{max_name}:{max_val} ")
print(f"Lowest GPA-{min_name}: {min_val}")

