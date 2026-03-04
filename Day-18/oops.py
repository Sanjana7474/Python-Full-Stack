class Flipkart:
    discount=10
    
    @classmethod
    def updatediscount(cls,newdiscount):
        cls.discount=newdiscount
        
    def userinfo(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
        print(f'Username: {self.name}')
        print(f'Phone Number: {self.phone_number}')

    @staticmethod
    def banner():
        print("Welcome to the Filpkart\n10% discount is going on,shop now")

p=Flipkart()
s=Flipkart()
