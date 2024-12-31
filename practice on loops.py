# # 1

# for x in range(1500 , 2700):
#     if(x%7 == 0):
#         print(x)
#         if(x%5 == 0):
#             print(x)

# # 2 

# sum = 0
# for i in range(10 , 21):
#     if(i %2 == 0):
#         sum = sum + 0
#         i = i + 1
# print(sum)

# # 3 
# i = 10
# sum = 0
# while i <= 20:
#     if(i %2 == 0):
#         sum = sum + i
#         i += 1
# print(i)

# # 4 
# sum = 0
# for i in range(2,20):
#     sum = sum + i
#     i = i+1
# print(sum)

# # 5
# list = [1 , 2 ,3 ,4 ,5]
# for x in list:
#     sqaure = x**2
#     print(sqaure)

# # 6
# sum = 0 
# list = [1 , 2 ,3 ,4 ,5]
# for i in list:
#     sum = sum + i
#     size = len(list)
#     ave = sum/size
# print(ave)

# # 7

# for i in range(20):
#     if(i%2 == 0):
#         print(i)
    




# list = [1 , 2 ,3 ,4 ,5 , 6 , 7,8, 15 , 16]
# for i in list:
#     if(i > 15):
#         break
#     else:
#         print(i)


# name = "school"
# count = 0
# for i in name:
#     if i != "o":
#         continue
#     else:
#         count= count+1
# print(count)


# list = [1 , 2 ,3 ,4 ,5 , 6 , 7,8, 15 , 16]
# for i in reversed(list):
#     print(i)


# f = int(input("enetr a numner"))
# c = (f -32)* (5/9)
# print(c)
 

# # print upto range numbers 
# for i in range(10, 16 , 2):
#     print(i , end = " ")

# # count of total list 
# list = [1 , 2, 3, 4,5,  6]
# for i in range(len(list)):
#     print(list[i])

# # order 
# row = 7
# for i in range(7):
#     for j in range(i):
#         print(j , end=' ')
#     print('')


# # while loop 
# num = 180 
# i = 0 
# while num > 10:
#     num = num/3 
#     i = i + 1
# print(i)

# #  print reverse 
# n = int(input("enter a num"))
# i = 10
# while i >= n:
#     print(i)
#     i = i - 1
        

# n = int(input("enter a num"))
# i= 1
# while i <= n:
#     if(i %2 == 0):
#         print(i)
#     i = i + 1

# # sum of odd numbers 
# n = int(input("enter a num"))
# i = 1 
# sum = 0
# while i<=n:
#     if(i%2 != 0):
#      sum = sum + i
#     i = i + 1 
# print(sum)

# #  sum of digits
# n = int(input("enter a num"))
# i = 1 
# sum = 0
# while i<=n:
#     sum = sum + i
#     i = i + 1
# print(sum)


# n = int(input("enter a number"))
# last_num = n % 10
# first_num = n/10
# print(last_num , float(first_num) , end =" ")

# # print element of list using for loop
# list = [1 , 2,3 ,4 ,5 ,6]
# for i in list:
#     print(i)

# # Calculate the product of elements in a list using a for loop:
# list = [1 , 2,3 ,4 ,5 ,6]
# product = 1
# for i in list:
#     product *= i
# print(product)
    

# # Print even numbers from 1 to 10 using a for loop:
# for i in range(2,11,2):
#     print(i)
   
# # Print numbers in reverse from 10 to 1 using a for loop:
# for i in range(10,0,-1):
#     print(i)

# # Print characters of a string using a for loop:
# name = "muzkeer"
# for i in name:
#     print(i)


# # Find the largest number in a list using a for loop:
# list = [1,2,3,4,5,6]
# largest = list[0]
# for i in list:
#     if i > largest:
#         largest = i 
# print(largest)

# # Find the average of numbers in a list using a for loop
# list = [1,2,3,4,5,6]
# sum = 0 
# size = len(list)
# for i in list:
#     sum = sum + i 
#     ave = sum/size
# print(ave)


# #  Print all uppercase letters in a string using a for loop:
# name = "MUZKeer"
# for i in name:
#     if i.isupper():
#         print(i)

# # finding vowels 
# name = "questions"
# vowel = "AEIOUaeiou"
# count = 0
# for i in name:
#     if i in vowel:
#         count = count + 1
# print(count)

# # Print a pattern of stars using nested for loops:
# for i in range(20):
#     for j in range(i + 1):
#         print(j , end = " ")
#     print()

# # Calculate factorial of a number using a while loop
# num = 5
# factorial = 1
# while num > 0 :
#     factorial *= num
#     num -= 1
# print(factorial)        


# #  Calculate the sum of numbers from 1 to 100 using a while loop:
# i = 1 
# sum= 0 
# while i <= 100:
#     sum = sum + i 
#     i = i + 1 
# print(sum)

# #  Find the first occurrence of a number in a list using a while loop:
# list = [1 , 2, 3, 4, 5, 6, 7]
# num = 5
# index = 0
# while index < len(list):
#     if list[index] == num:
#        break
#     index += 1
# else:
#     index = -1
# print(index)


# # Find all prime numbers between 1 and 50 using nested for and if:
# for num in range(2, 51):
#     for i in range(2 ,num):
#         if num % i == 0:
#             break
#     else:
#         print(num)        


# #  Print numbers divisible by 3 or 5 from 1 to 20 using a for loop:
# for i in range(1 , 21):
#     if (i%3== 0 or i %5== 0):
#         print(i)

# #  Print a list of squares of numbers from 1 to 5 using a list comprehension:
# list = [1 ,2 ,3 ,4]
# for i in list:
#     suare = i**2
#     print(suare)

# #  Print the Fibonacci sequence up to the 10th term using a while loop:
# a , b = 0 , 1
# i = 0
# while i < 10:
#     print(a , end=" ")
#     a , b = b , a+b 
#     i = i + 1


# # Find the common elements in two lists using a for loop:
# list1 = [1 , 2,3,4 , 5,6,7]
# list2 = [1 , 2,3,4 , 5, 6,7 ,5,6,7]
# empty = []
# for ele in list1:
#     if ele in list2:
#         empty.append(ele)
# print(empty)

# # Print numbers in a list until a negative number is encountered using a while loop:
# list = [1 ,2 ,3 ,4 ,5,6 ,-1 ,2, 3]
# index = 0
# while list[index] > 0:
#     print(list[index])
#     index = index + 1
    
# #  Print numbers from 1 to 5, except 3 using a for loop and continue statement:
# for i in range(1 , 6):
#     if (i == 3):
#         continue
#     else:
#         print(i)

# # Print numbers from 1 to 10. If a number is divisible by 4, stop the loop using a for loop and break statement:
# for i in range(1, 11):
#     print(i)
#     if i % 4 == 0:
#         break
    
# #Print numbers from 1 to 10. If a number is even, skip it using a for loop and else clause:
# for i in range(1 , 11):
#     if i % 2 == 0:
#         continue
#     print(i)
# else:
#     print("sucess")
    
# #  Print numbers from 1 to 10. If a number is even, break the loop using a for loop and else clause:
# for i in range(1 , 11):
#     if i % 2 == 0:
#         break
#     print(i)
# else:
#     print("the loop is successfully breaked")


# # calculate the sum 
# sum = 0 
# for i in range(1 , 101):
#     sum = sum + i 
# print(sum)

# # multiple table
# num = 5
# for i in range(1 ,11):
#     mul = i * num
#     print(num , "*" , i , "=" , mul)

# # list reverse 
# list = [1 , 2,3 ,4 ,5,6]
# for i in range(len(list) -1, -1 , -1):
#     print(list[i])

# # fibonacci
# a , b = 0 , 1
# i = 0
# while i <= 10:
#     print(a ,end=" ")
#     a , b = b , a + b
#     i = i + 1

## factorial 
# i = 1
# fact = 1
# while i <=5:
#     fact = fact * i 
#     i = i + 1
# print(fact)

# dict = {
#     "name" : "muzkeer",
#     "age" : 24 ,

# }
# for key,value in dict.items():
#     print(key,value)
       
# # zipping 
# list1 = [ "name" , "age" , "place" ]
# list2 = ["muzkeer" , 17 , "kavali"]
# for name,value in zip(list1,list2):
#     print(f"{name} is {value} over!")

# list1 = [ "name" , "age" , "place" ]
# for i in range(len(list1)):
#     print(list1[i])

# for i in range(5 , 0 , -1):
#     print(i)

# i = 0
# while i < 5:
#     if i == 3:
#         continue
#     print(i)
#     i = i + 1

# list1 = [ "name" , "age" , "place" ]
# for i in list1:
#     print(i , end = " ")

# for i in range(3):
#     for j in range(2):
#         print(i , j)

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# list = [1 , 2, 3, 4, 5, 6, 7, 8,9 ]
# a , b = 0 , 0
# for i in list:
#     if i %2 == 0:
#         a = a+ 1 
#     else:
#         b = b + 1 
# print(a , b)

# for i in range(2, 15):
#     for j in range(2 , i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

## perfect number
# n = int(input("enter a number"))
# sum = 0
# for i in range(1 , n):
#     if(n%i == 0):
#         sum = sum + i 
# if sum == n:
#     print("it is a perfect number")
# else:
#     print("not")


# num = input("enter a number")
# rever = str(num)[::-1]
# if (num == rever):
#     print("it id")
# else:
#     print("not")
# for i in range(65 , 91):
#     print(chr(i))


# n = 407
# size = len(str(n))
# sum = 0 
# i = n
# while i > 0: 
#     last = i % 10
#     sum = sum + last**size 
#     i //= 10
    

# if n == sum:
#     print(n, "yes")
# else:
#     print(n, "not")

import math

num = int(input("enter a number"))
for i in range(1 , num):
    sum = 0
    fact = 1 
    temp = i
    while temp > 0:
        remainder = temp % 10
        fact = math.factorial(remainder)
        sum = sum + fact 
        temp = temp // 10
    if sum == num:
        print(num , "yezz")
    else:
        print(num , "not")


    
    