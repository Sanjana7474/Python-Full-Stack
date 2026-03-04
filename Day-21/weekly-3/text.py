'''with open("example.txt") as file:
    data=file.read()
    print(data)'''
    
'''with open("example.txt","r") as file:
    for line in file:
        print(line.strip())'''

'''import json

students=[
    {"name":"Pooja","age":23},
    {"name":"Dudu","age":23}
    ]
with open("students.json","w") as file:
    json.dump(students,file,indent=5)'''
'''import json

with open("students.json","r") as file:
    data=json.load(file)
    print(data)
for student in data:
    print(student["name"],student["age"])'''
'''import json
with open("students.json","r") as file:
    data=json.load(file)
new_student={"name":"Teju","age":26}
data.append(new_student)
with open("students.json","w") as file:
    json.dump(data,file,indent=4)'''
'''import csv
with open("students.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Name","Age","Grade"])
    writer.writerow(["Bob",23,"A+"])'''
'''import csv
with open("students.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
         print(row)'''
'''import csv
with open("students.csv","a",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Pooja",23,"O"])'''
'''import csv
with open("students.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row["Name"],row["Grade"])'''

import csv
with open("students.csv","w",newline="") as file:
    fieldnames=["Name","Age","Grade"]
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name":"stalin","Age":23,"Grade":"C"})
    

