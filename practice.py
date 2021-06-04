class LoggedError(Exception):
    def __init__(self,value):
        self.value=value
    
    def __str__(self):
        return repr(self.value)
    
class Member(object):
    nextId=0
    
    def __init__(self):
        self.id=Member.nextId
        Member.nextId+=1
    
    def getid(self):
        return self.id
    
class Customer(Member):
    
    def __init__(self,email,password):
        Member.__init__(self)
        self.email=email
        self.customerdic={}
        self.customerdic[self.email]=password
        self.logged=True
        
    def signin(self,email,password):
        if self.customerdic[self.email]==password:
            if self.logged==True:
                self.logged=False
                return True
                
            else:
                raise LoggedError('Already signed in') 
        else:
            return False
            
    
    def signout(self):
        if self.logged==True:
            raise LoggedError('Already signed out')
        else:
            pass

    def __str__(self):
        return self.email
    
c1 = Customer("abc@abc.com", "12341234")
c2 = Customer("def@def.com", "56785678")
c3 = Customer("hello@world.com", "qwerty")
print("Customer 1 is {}".format(c1))
print("Customer 2 is {}".format(c2))
print("Customer 3 is {}".format(c3))
print("Customer 1's id is {}".format(c1.getid()))
print("Customer 2's id is {}".format(c2.getid()))
print("Customer 3's id is {}".format(c3.getid()))
try:
    print("Customer 1 sign-in {}".format(c1.signin("abc@abc.com", "12341234")))
except LoggedError as e:
    print(e)
    
try:
    print("Customer 2 sign-out {}".format(c2.signout()))
except LoggedError as e:
    print(e)
    
try:
    print("Customer 3 sign-in {}".format(c3.signin("abc@abc.com", "12341234")))
except LoggedError as e:
    print(e)
