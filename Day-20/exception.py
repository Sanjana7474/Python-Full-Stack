class Snapchat:
    def __init__(self,username,password,friends):#constructor
        self.username = username#public
        self.__password = password#private
        self._friends = friends#protected
    def getpassword(self):
        return self.__password
    def setpassword(self,new_password):
        self.__password=new_password
    @property#particular friends
    def oprFriends(self):#property setting
        return self._friends
    @oprFriends.setter
    def oprFriends(self,newfriend):
        self._friends.append(newfriend)
        
pooja = Snapchat('Poojitha','12345',['Teju','Dudu'])
#public
print(f'Name before modification: {pooja.username}')
pooja.username='Kerrthi'
print(f'Name after modification: {pooja.username}')

#private
print(f'Password before modification: {pooja.getpassword()}')#can't access out side we can access class inside. so we use method then we can access the private attributes
pooja.setpassword('P@123')
print(f'Password after modification: {pooja.getpassword()}')

#protected
print(f'Friends before modification: {pooja.oprFriends}')
pooja.oprFriends='Poojitha'
print(f'Friends after modification: {pooja.oprFriends}')



        
