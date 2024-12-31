# # 1 
# age = int(input("enter your number"))
# print("major") if (age > 18) else print("minor")
# # 2
# x = int(input("enter a number"))
# y = int(input("enter another number"))
# z = x + y
# if (x == y):
#     print(z*2)
# elif(x != y):
#     print(z)

# # 3 
# num = int(input("enter a number"))
# nums = num - 15
# if (num >= 15):
#     print(nums*2)
# else:
#     print(nums * -1)

# # 4 
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

# # 5 
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

# # 6 
# val1 = input("enter value T or S or  R ")
# area = "1/2 x a x b"
# areaofsquare = "s x s"
# areaofrectanle = "l x b"
# if(val1 == "T"):
#     print(area)
# elif(val1 == "S"):
#     print(areaofsquare)
# elif(val1 == "R"):
#     print(areaofrectanle)

# # 7
# x = int(input("enter a number"))
# y = int(input("enter a number"))
# z = int(input("enter a number"))
# if (x > y and x > z):
#     print("x is bigger")
# elif( y> x and y > z):
#     print("y is bigger")
# elif(z > x and z>y):
#     print("z is bigger")

# # 8
# num = int(input("enter a number"))
# nums = num%10
# if(nums%3 == 0):
#     print("divisible")

# # 9
# num = int(input("enter a number"))
# if (num == 1):
#     print("sunday")
# elif(num == 2):
#     print("monday")
# elif(num == 3):
#     print("tuesday")
# elif(num == 4):
#     print("wednesday")
# elif(num == 5):
#     print("thursday")
# elif( num == 6):
#     print("friday")
# elif(num == 7):
#     print("saturday")

# # 10
# num = int(input("enter FOUR NUMBERS "))
# b = num%10 
# c = num//10 
# d = c%10 
# e = c//10
# f = e%10 
# g = e//10
# print(b,d,f,g ,end="") 

# # 11
# num = int(input("enter a number"))
# if( num % 7 == 0 and num % 5 == 0):
#     print("yes")
# else:
#     print("no")

# # 12
# num = int(input("enter a number"))
# if(num % 4 == 0 or num % 400 == 0):
#     print("it is a leap yar")
# else:
#     print("it is not")

# 13
# unit = int(input("enter your units"))
# if(unit <= 100):
#     print('no charges')
# elif(unit <100 and unit >=200):
#     cost = unit-100
#     total = cost*5
#     print(total)
# else:
#     cost2 = unit - 200
#     total2 = cost2*10
#     print(total2 + 500)

# 14
# cost_price = int(input("enter a number"))
# if(cost_price > 100000):
#     print("tax" , cost_price * 0.15)
# elif(cost_price > 50000 and cost_price <= 100000):
#     print("tax" , cost_price * 0.1)
# else:
#     print("tax" , cost_price * 0.05)

# 15

# age after 100 years
# name = input("enter a name")
# age = int(input("enter a age as on 2020"))
# after_100 = 100 - age 
# print(name , "you will turn 100 years at the age of " , after_100+2020)

# 16
# popcorn GST
# type_of_popcorn = str(input("enter your type"))
# if(type_of_popcorn == "salted"):
#     print("total amount" , 20+(5/100))
# elif(type_of_popcorn == "packaged"):
#     print("total amount" , 40+(12/100))
# elif(type_of_popcorn == "caramel"):
#     print("total amount" , 150+(18/100))

# 17
# # tax in cab 
# basefare = int(input("enter a fare of 100rs in 6km"))
# range = input("rural or outstation")
# if(range == "rural"):
#     rural = basefare - 6
#     amount = rural * 20 
#     print("your total" , amount+100)
# elif(range == "outstation"):
#     outstation = basefare - 6
#     amount = outstation * 10
#     print("your total" , amount+100)

# 18
# timeperiod = int(input("enter your working service"))
# salary = int(input("enter your salary"))
# if(timeperiod >= 10):
#     print("total bonus" , salary*0.1)
# elif(timeperiod >=6 and timeperiod<=10):
#     print("total bonus" , salary*0.08)
# else:
#     print("total bonus" , salary*0.05)

# 19
# days = int(input("enter a number"))
# if(days <= 5):
#     print(days*2)
# elif(days > 6 and days <= 10):
#     print(days*3)
# elif(days >11 and days <=15):
#     print(days*4)
# else:
#     print(days*5)

# 20
kilometers = int(input("enter a distance"))
if(kilometers <= 10):
    amount = kilometers*11
    print(amount)
elif(kilometers > 10 and kilometers <=100):
    print((kilometers - 10)*10 - 110)
else:
    print(kilometers*9)

# 21
# units = int(input("enter a num"))
# if(units <= 100):
#     print("FREE")
# elif(units > 100 and units <= 200):
#     unit = units - 200
#     print(unit*2)
# else:
#     cost = units - 300
#     total = cost*5
#     print(total+400)


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


# num_of_cls_held = int(input("enter a number"))
# num_of_cls_attend = int(input("enter a number"))

# total = num_of_cls_attend /num_of_cls_held
# per = total*100
# if(per >= 75):
#     print("you are allowed to sit in the class")
# else:
#     print("you are not allowed to sit in the cLASS")