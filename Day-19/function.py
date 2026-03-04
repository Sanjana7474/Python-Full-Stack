'''class Flipkart:
    discount=10
    
    @classmethod
    def updatediscount(cls,newdiscount):
        cls.discount=newdiscount
        print(f'{cls.discount} updatediscount')
        
    def userinfo(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
        print(f'Username: {self.name}')
        print(f'Phone Number: {self.phone_number}')

    @staticmethod
    def banner():
        print("Welcome to the Filpkart\n10% discount is going on,shop now")

p=Flipkart()
p.userinfo('p',9398645349)

p.updatediscount(30)
p.updatediscount(40)

p.banner()
Flipkart.banner()

s=Flipkart()'''
'''
#constructor
#It is a special method automatically call the function,whenever create an object
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        print(f"Hey {self.username}, Welcome to the Instagram!!!")
pooja=Instagram('Pooja123','binnu@123')
dudu=Instagram('Dudu0316', 'dudu@0316')'''

'''#Inheritance
class InstagramV1:
    def __init__(self,username):
        self.username=username
        print(f"Hey {self.username}, Welcome to the Instagram!!!")
        
    def reels(self):
        print("You can upload and scroll the reels")
        
    def posts(self):
        print("You can post your pics")
        
class InstagramV2(InstagramV1):
    def __init__(self,username):
        super().__init__(username)#InstagramV1.__init__(self,username) class name
        
    def story(self):
        print("You can upload the story")#single inheritance

class InstagramV3(InstagramV2):
    def __init__(self,username):
        super().__init__(username)

    def note(self):
        print("You can upload a note")#Multi level inheritance

class Live:
    def launchlive(self):
        print("Now you can go on live")
class Verification:
    def verify(self):
        print("You can verify your account for better features")
class InstagramV4(InstagramV3,Live,Verification):
    def __init__(self,username):
        super().__init__(username)#Multiple inheritance

class Creator(InstagramV4):
    def __init__(self,username):
        super().__init__(username)
    def insights(self):
        print("You can check your post insights")


class Business(InstagramV4):
    def __init__(self,username):
        super().__init__(username)
    def buttons(self):
        print("you can contact them mail and number")#hiearichal inheritance
    
        
        
        
pooja=InstagramV1('Pooja')
pooja.reels()
pooja.posts()

dudu=InstagramV2('Dudu')
dudu.reels()
dudu.posts()
dudu.story()

bubu=InstagramV3('Bubu')
bubu.reels()
bubu.posts()
bubu.story()
bubu.note()

stalin=InstagramV4('Stalin')
stalin.reels()
stalin.posts()
stalin.story()
stalin.note()
stalin.launchlive()
stalin.verify()

keerthi=Creator('Keerthi')
keerthi.reels()
keerthi.posts()
keerthi.story()
keerthi.note()
keerthi.launchlive()
keerthi.verify()
keerthi.insights()

naga=Business('Naga')
naga.reels()
naga.posts()
naga.story()
naga.note()
naga.launchlive()
naga.verify()
naga.buttons()'''


#overloading


#Polymorphism-overriding same method different actions
class Hotstar:
    def __init__(self,username):
        print(f'Hey {username}, Welcome to the Hotstar')
    def playvideo(self):
        print("Ads wil be run")
        print("Quality is low")
        print("No download option")
        print("No multiple logins")
    def search(self):
        print("You can search for program")
    def watchlist(self):
        print("You can add the movies to watchlist")
    def notifications(self):
        print("You can get the push notifications")
    def login(self):
        print("You can login to the Hotstar")

class PremiumHotstar(Hotstar):
    def __init__(self,username):
        print(f'Hey {username}, Welcome to the Premium Hotstar')
    def playvideo(self):
        print("Ads won't run")
        print("Quality is High")
        print("Download option")
        print("Multiple logins")

pooja=Hotstar("Pooja")
pooja.playvideo()
pooja.search()
pooja.watchlist()
pooja.notifications()
pooja.login()

dudu=PremiumHotstar("Dudu")
dudu.playvideo()
dudu.search()
dudu.watchlist()
dudu.notifications()
dudu.login()
        
    

























































