# i = 16
# if (i > 18):
#     print("eligible to vote")

# i = 19
# if i > 18:
#     print("you are a major")
# else:
#     print("not major")

# # nesting 
# j = 25
# if j<25:
#     if(j<20):
#         print("J is less than 20")
#     if (j <10):
#         print("J is less than 10 too")

# k = 25
# if (k == 30):
#     print("you will get dosa")
# elif(k ==25):
#     print("you will get puri")
# elif(k == 20):
#     print("you will get idly")
# else: 
#     print("give valid amount")

# # short hand if (writing statements in a single line)
# l = 21
# if (l >= 18):print("your eligible to get driving license") 

# # short hand if and else (writing statements in a single line)
# n = 12
# print("even") if (n%2 == 0) else print("odd") # no need to add collen

# # unsolved 1 
# l = float(input("length"))
# b = float(input("breadth"))
# if (l ==b):
#     print('square')
# else:
#     print("not square")

# # unsolved 2 
# n = float(input("enter a number"))
# m = float(input('enter a another number'))
# if (n > m ):
#     print("n is greater")
# else:
#     print("m is greater")

# # unsolved 3 
# quantity = float(input("enter a quantity"))
# cost = quantity * 100 
# discount = cost - quantity*10
# print(discount) if (cost > 1000) else print(cost)

# #  unsolved 4 
# salary = float(input("enter your salary"))
# yearofservice = float(input("enter your service"))
# bonus = salary*5/100
# if(yearofservice > 5):
#     print(bonus)
# else:
#     print(salary)


# #  unsolved 5
# x = float(input("enter your age"))
# y = float(input("enter your age"))
# z = float(input("enter your age"))
# if (x > y and x > z):
#     print("x is oldest")
#     if (y < z):
#         print("y is youngest")
#     else:
#         print("z is youngest")
# if (y > x and y > z):
#     print("y is oldest")
#     if (x < z):
#         print("x is youngest")
#     else:
#         print("z is youngest")
# if (z > x and z > y):
#     print("z is oldest")
#     if (x < y):
#         print("x is youngest")
#     else:
#         print("y is youngest")

# # unsolved 6
# user = float(input("enter a numner"))
# user = user*-1
# print("INPUT :" ,user)

# unsolved 9
# age = int(input("enter your age"))
# sex = str(input("enter your gender"))
# maritalstatus = input("enter a number")
# if (sex == "F") :
#     print("you can work in urban area")
# elif(sex == "M"  , age <= 20 and age >40):
#        print("you can work anywhere")
# elif(sex == "M"  , age<=40 and age > 60):
#        print("you will work in urban ")
# else:
#         print("ERROR")

#  7
# user = int(input("enter a numner"))
# if (user < 0):
#     print("the result is" , user*-1)
# # else:
#     print(user)
#  8
# held = int(input("entre cls"))
# attended = int(input("enter"))
# medical = str(input("enter a medical"))
# p = (attended/held)*100
# if (medical == "Y"):
#     print("you able to sit")
# else:
#     if (p >= 75):
#         print("allow")
#         print("your pecentage is " , p)
#     else:
#         print("you are notk allowed to write the exam")
#         print("your percentage" , p)
# a = int(input("enter"))
# b = int(input("enter"))
# sum = a + b
# if (a == b):
#     print(sum*2)
# else:
#     print(sum)
# n = int(input("enter a number"))
# diff = 15 - n 
# if (n >= 15):
#     print(diff * -2)
# else:
#     print(diff)
# a = int(input("enter"))
# b = int(input("enter"))
# c = int(input("enter"))
# list = [13 , 14 ,16 , 17 , 18 ,19]
# sum = a + b + c
# if (a in list and b in list and c in list):
#     print(sum * 0)
# elif(a in list and b in list and c not in list):
#     print(c)
# elif(a in list and b not in list and c in list):
#     print(b)
# elif(a not in  list and b in list and c in list):
#     print(a)
# elif(a not in list and b not in list and c in list): 
#     print(a + b)
# elif(a not in list and b in list and c not in list):
#     print(a + c)
# elif(a in list and b not in list and c not in list):
#     print(b + c)
# else: 
#     print(sum)
# 5 
# a = int(input("enter"))
# b = int(input("enter"))
# c = int(input("enter"))
# sum = a + b + c
# if ( a == b and b == c and c == a):
#     print(sum* 0)
# elif(a == b):
#     print(c)
# elif(b == c):
#     print(a)
# elif(c == a):
#     print(b)
# else:
#     print(sum)
#  6 
# val1 = str(input("enter a value T or S or R"))
# areaoft = "1/2 * base *height"
# areaofs = "area of square == s*s"
# areaofr = "area of rectangle == l*b"
# if (val1 == "T"):
#     print(areaoft)
# elif (val1 == "S"):
#     print(areaofs)
# elif (val1 == "R"):
#     print(areaofr)

# a = int(input("enter"))
# b = int(input("enter"))
# c = int(input("enter"))
# if(13<= a <= 14 or 16<=a<=19)and(13<=b<=14 or 16<=b<=19)and(13<=c<=14 or 16<=c<=19):
#     print(0)
# elif(13<= a <= 14 or 16<=a<=19)and(13<=b<=14 or 16<=b<=19):
#     print(c)
# elif(13<=b<= 14 or 16<=b<=19)and(13<=c<=14 or 16<=c<=19):
#     print(a)
# elif(13<=c<= 14 or 16<=c<=19)and(13<=a<=14 or 16<=a<=19):
#     print(b)
# elif(13<= a <= 14 or 16<=a<=19):
#     print(b+c)
# elif(13<=b<= 14 or 16<=b<=19):
#     print(a+c)
# elif(13<=c<= 14 or 16<=c<=19):
#     print(a+b)
# else:
#     print(a+b+c)

# n = int(input("enter a number"))
# if n %2 == 0:
#     print("it is even") 
# else:
#     print("it is not a even")

# n = int(input("enter a number"))
# if (n %7==0 and n%5 == 0):
#     print("it is divisibe by 7 and multiple of 5 ")
# else:
#     print("not a divisible and multiple")

# n = int(input("enter a number"))
# if n > 0:
#     print("it is positive")
# elif n < 0 :
#     print("it is negative")
# else:
#     print("it is zero")

a = int(input("enter"))
b = int(input("enter"))
print(a > b and b < a)
print(a > b or a == b)
print(not(a == b))
