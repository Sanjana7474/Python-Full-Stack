'''Customername=input("Name: ")
Customerage=int(input("Age: "))
Productprice=float(input("Price:"))
Itemspurchased=eval(input("Items: "))
Uniquecoupons=eval(input("Coupons: "))
Deliveraddress=eval(input("Address: "))'''

'''Monthlysalary=int(input("Monthly Salary: "))
ExistingLoan=int(input("Existing Loan: "))
Creditscore=int(input("Credit Score: "))
if Monthlysalary>30000 and Creditscore>700 and  ExistingLoan<50000:
    print("Eligible")
else:
    print("Not Eligible")'''




'''units=int(input("Enter the units: "))
bill=0
if 0<units<=100:
    bill=units*3

elif 100<units<=200:
    bill=300(units-100)*5

elif 200<units<=300:
    bill=300+500+(units-200)*7

elif units>300:
    bill=300+500+700+(units-300)*10

gst=bill+bill*0.5
if gst>500:
    print(f"Final Bill{included gst: {gst-500}" )
else:
    print(f"Final Bill(included gst):{gst}")'''


'''for i in range(3):
    username=input("Enter the username:")
    password=input("Enter the password:")
    if username=='admin' and password=='PFS48':
        print("Login Successful")
        break
else:
    print("Account Locked")'''


'''
balance=10000
while True:
    amount=int(input("Enter the amount: "))
    if amount==0:
        break
    if amount<=balance:
        print(f"{amount} withdraw successfully")
        balance-=amount
        print(f"current balance: {balance}")
    else:
        print("Insufficient Balance")'''




'''amount=int(input("Enter the amount: "))
note2000=amount//2000
amount=amount%2000
note500=amount//500
amount=amount%500
note200=amount//200
amount=amount%200
note50=amount//50
amount=amount%50
print(note2000,note500,note200,note50)

if amount!=0:
    print("no money")'''




notes=[2000,500,200,100,50,20,10]
amount=int(input("Enter the amount:"))
for i in notes:
    feq=amount//i
    if feq>0:
        print(f"{i}*{feq}")
        amount=amount%i
    
    
    















    
