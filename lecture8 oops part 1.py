# class Factory: 
#     cars = "ford"
#     color = "blue"

# car = Factory()
# print(car.color)
# print(car.cars)

# constuctor 
# class Family:
#     schoolname = "narayana"
#     def __init__(self , fullname):
#         self.name = fullname
#         print("i am a student")

#     def hello(self):
#         print("hello" , self.name)

#     def welcome(self):
#         return self.name

# s1 = Family("abba")
# print(Family.schoolname)
# print(s1.name)
# s1.hello()
# print(s1.welcome())

class Number():
    def __init__(self , bal , account):
        self.balance = bal
        self.acco_no = account

    def debit(self , amount):
        self.balance -= amount
        print("your", amount ,"was debited" )
        print("total balance" , self.get_balance())


    def credit(self , amount):
        self.balance += amount
        print("your" , amount ,"was credited")
        print("total balance" , self.get_balance())


    def get_balance(self):
        return self.balance
    
   
    
n1 = Number(100000 , 100)
print(n1.balance)
print(n1.acco_no)

n1.debit(1000)


# to del a property and objects 
# class Name():
#     def __init__(self, name):
#         self.name = name
    
# s1 = Name("pallu")
# print(s1.name)
# del s1.name
# print(s1.name)

# inheritance 
class Car:
    @staticmethod
    def start():
        print("started")

    @staticmethod
    def stop():
        print("stopped")

class Tuyato(Car):
    def __init__(self , name ):
        self.name = name


c1 = Tuyato("fortuner")
print(c1.name)

print(c1.start())


# types of inheritance 
#  multi - inheritance
class Car:
    @staticmethod
    def start():
        print("started")

    @staticmethod
    def stop():
        print("stopped")

class Tuyato(Car):
    def __init__(self , name):
        self.name = name


class fortuner(Tuyato):
    def __init__(self , brand):
        self.brand = brand

c1 = fortuner("petrol")
print(c1.brand)
c1.start()

# multiple inheritance 
# class Name():
#     var1 = "muzkeer"

# class Mul():
#     var2 = "majahar"

# class mulp(Name , Mul):
#     var3 = "momin"

# c1 = mulp()
# print(c1.var3)


# super method 
class Car:
    def __init__(self,type):
        self.type =type 

    @staticmethod
    def start():
        print("started")

    @staticmethod
    def stop():
        print("stopped")

class Tuyato(Car):
    def __init__(self , name , type):
        super().__init__(type)
        self.name = name

c1 = Tuyato("ford" , "electric")
print(c1.name)
print(c1.type)


# class method 
class Car:
    name = "muzkeer"
    def ate(cls , name):
        cls.name = name

p1 = Car()
p1.ate("majahar")
print(p1.name)

# propety
class Car:
    def __init__(self , maths , phy):
        self.maths = maths
        self.phy = phy
    
    @property
    def percentage(self):
        return  str((self.maths + self.phy) / 3)
    

p1 = Car(44 , 45)

print(p1.percentage)

# polymerphism 
class Car:
    def __init__(self , real , img):
        self.real = real
        self.img = img
    
    def number(self):
        print(self.real, "i +" ,self.img ,"j")
        

    def __add__(self , num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Car(newreal , newimg)
       



num1 = Car(2 , 3)
num1.number()

num2 = Car(4 , 5)
num2.number()

num3 = num1 + num2
num3.number()
    
    

    
