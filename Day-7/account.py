data={
    123456:{'pin':1234,'balance':5000,'history':[]},
    345678:{'pin':4321,'balance':10000,'history':[]},
    892345:{'pin':3214,'balance':20000,'history':[]},
    }
def check_balance(acc):
    print(f"Your Balance Amount is ${data[acc]['balance']}")
def deposit(acc):
    amount=int(input("Enter the amount:"))
    data[acc]['balance']+=amount
    data[acc]['history'].append(f"{amount} is deposited")
    print(f"{amount) is deposited successfully")
def withdraw(acc):
    amount=int(input("Enter the amount:"))
    data[acc]['balance']-=amount
    data[acc]['history'].append(f"{amount} is withdraw") 
    print(f"{amount) is withdraw successfully")
else:
    print("You don't have enough balance')
def view_history(acc):
    if data[acc]['history']:
        print("------------Transaction History-----------")
        for i in data[acc]['history']:
            print(i)
        else:
           print("---------End of history-----------")
    else:
        print("No Transactions")
def setpin(acc):
    new_pin=int
    
    
        
def menu():
    print('1.Check Balance\n2.Deposit\n3.Withdraw\n4.Set Pin\n5.View Transactions\n6.Exit')
print('Welcome to the ATM')
acc=int(input("Enter the account number:"))
pin=int(input("Enter the pin:"))
if acc in data and data[acc]['pin']==pin:
    print("Login Successfully")
while True:
    menu()
    ch=int(input("Enter the choice:"))
    if ch==1:
        check_balance(acc)
    elif ch==2:
        deposit(acc)
    elif ch==3:
        withdraw(acc)
    elif ch==4:
        
    elif ch==5:
        view_history(acc)
    elif ch==6:
        print("Thankyou")
        break
else:
    print("Invalid login. Try Again")
