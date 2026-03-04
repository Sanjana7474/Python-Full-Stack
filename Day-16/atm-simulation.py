while True:
    print("---------ATM Simulation Menu--------")
    print("1. Check Average Transaction (ZerodivisionError))
    print("2. Withdraw with Invalid Input(valueError))
    print("3. Deposit with Invalid Data Type(TypeError))
    print("4. Access Invalid Transaction History(Indexerror))
    print("5. Access Non-Existent Account (Keyerror))
    print("6. Read Missing transaction Log File (FileNotFoundError))
    print("7. Exit")
    ]
    ch=int(input("select an option (1-7):"))
    if ch=="1":
          zero_division_error_case()
    elif ch=="2":
        value_error_case()
    elif ch=="3":
        type_error_case()
    elif ch=="4":
        index_error_case()
    elif ch=="5":
        key_error_case()
    elif ch=="6":
        file_not_found_error_case()
    elif ch=="7":
        print("Exiting the ATM Simulation. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid choice.")
        
def  zero_division_error_case():
    try:
        transactions=[]
        average_transaction=sum9transactions) / len(transactions)
        print("Average transaction:", average_transaction)
    except ZeroDivisionError:
        print("Error: cannot calculate average transaction because there are no")
def value_error_case():
    try:
        withdrawal_amount=int("100 /")
        print("Withdrawing:", withdrawal_amount)
    except ValueError:
        print("Error: Invalid value entered. Please enter a numeric amount.")
def type_error_case():
    try:
        balance=500
        deposit_amount="100"
        new_balance=balance+deposit_amount
        print("New Balance:",new_balance)
    except TypeError:
        print("Error: Incompatible data types cannot add string to an integer.")
def index_error_case():
    try:
        transaction_history=[200,-150,300]
        print("Last transaction:", transaction_history[5])
    except IndexError:
        print("Error : Trying to access a transaction that does not exist.")
def key_error_case():
    try:
        accounts={"12345":{"pin":"1111", "balance":1000}}
        account_number
