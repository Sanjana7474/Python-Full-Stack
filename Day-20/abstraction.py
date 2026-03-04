from abc import ABC,abstractmethod

class BankAccount(ABC):
    def checkbalance(self):
        print("\n\nYou can checkout your balance---------")
        
    @abstractmethod
    def deposit(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass
    
class SavingAccount(BankAccount):
    def deposit(self):
        print("2 lakhs per day")
    def withdraw(self):
        print("1 lakh you can withdraw")
        
class CurrentAccount(BankAccount):
    def deposit(self):
        print("unlimited deposit")
    def withdraw(self):
        print("unlimited withdraw")
        
class JointAccount(BankAccount):
    def deposit(self):
        print("only those 2 people can deposit")
    def withdraw(self):
        print("1-2 lakhs per day you can withdraw")
        
class SalaryAccount(BankAccount):
    def deposit(self):
        print("no limit")
    def withdraw(self):
        print("20k-1L per day")
        
class PensionAccount(BankAccount):
    def deposit(self):
        print("No deposit")
    def withdraw(self):
        print("40k per day")

print("---------------pooja-------------")
pooja = SavingAccount()
pooja.checkbalance()
pooja.deposit()
pooja.withdraw()

print("---------------keerthi-------------")
keerthi = CurrentAccount()
keerthi.checkbalance()
keerthi.deposit()
keerthi.withdraw()
print("---------------stalin_dudu-------------")
stalin_dudu = JointAccount()
stalin_dudu.checkbalance()
stalin_dudu.deposit()
stalin_dudu.withdraw()

print("---------------naga-------------")
naga = SalaryAccount()
naga.checkbalance()
naga.deposit()
naga.withdraw()

print("---------------Anjamma-------------")
Anjamma = PensionAccount()
Anjamma.checkbalance()
Anjamma.deposit()
Anjamma.withdraw()































