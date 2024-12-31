# # creating a function 
# def myvar():
#     print("hello world")
# myvar()
# # addition
# a = 2 
# b = 3
# def myfun():
#     sum = a + b 
#     print("sum of two numbers " , sum)
# myfun()

# def number(fclass):
#     print(fclass ,"welcome")
# number("muzkeer")

# def name():
#     print("hello world")
# name()

# #arguments 
# def myvar(name , age ):
#     print(name , age) 
# myvar("muzkeer" , 25)

# # unknown name 
# def myfun(*name):
#     print("my name is "+name[1])
# myfun("pallu" , "zunnu" , "muzkeer")

# def mydict(name1 , name2):
#     print("name is" + name2)

# mydict(name1 = "pallu" , name2 = "muzkeer")

##default parameter
# def fun(name = "muzkeer"):
#     print(name)
# fun()

# def mul(x):
#     pass

# def positonal(x):
#     print(x)

# positonal(x = 3)

# def zunnu(a , b):
#     return a * b 
# print(zunnu(1 ,3)


# def print_args(*args):
#     for arg in args:
#         print(arg)
# print_args(1 , 2, 3, 4)


# def muzkeer(name):
#     print("my name is " + name)
# def zunnu(func , valu):
#     func(valu)
# zunnu(muzkeer , "muzkeer")

# def varia(a  , b):
#     return a * b
# print(varia(1 , 3))

# def function(name = "muzkeer"):
#     print("my name is" + name)

# function("zunnu")
# function()

# def multi(a , b):
#     return a + b , a*b , a - b
# print(multi(1 ,4))

# def car(*bike , **cars):
#     print("my favorate bike is" +  bike[2])
#     print("my favorate car is" + cars["name2"])

# car("majahar" , "muzkeer", "zunnu" , name1 = "fararee" , name2 = "rolls royee")

# ## lamda 
# x = lambda a , b : a + b 
# print(x(1 , 2))

# x = lambda a , b : a * b 
# print(x(5,7))

# def myfun(n):
#     return lambda  a : a * n
# word = myfun(2)
# letter = myfun(3)

# print(word(11))
# print(letter(20)) 

# def functin(a , b):
#     try:
#       result = a/b
#     except ZeroDivisionError:
        
#        return "it cannot be divisible "
#     return result
# print(functin(10,0))

def fact(x):
    if x == 1:
        return 1 
    else:
        return x * fact(x - 1)
print(fact(10))

