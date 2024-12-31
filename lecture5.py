#  while loop 
# i = 1 
# n = int(input("enter a number"))
# while i <= n  :
#     mul = i *n
#     print(n , "*" , i , "=" , mul )
#     i += 1

# n = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x= 36
# i = 0 
# while i < len(n):
#     if(n[i] == 36):
#         print(i)
#     else:
#         print("finding")
#     i += 1

# i = 1 
# while i <= 10: 
#     if(i%2 == 0):
#         i = i + 1 
#         continue
#     print(i)
#     i = i + 1
        

#  for loop 
# string = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for num in string:
#         print(num)
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) it os also known as linear search
# x = int(input("enter a number")) 
# i = 0
# for num in tup: 
#     if(num == x):
#           print("value is", i )
#     i += 1 

#  range for loop
# for n in range(5): # range(stop) last value will be not included 
#       print(n)

# for n in range(2 , 20): # tange(start , stop)
#         print(n)

# for n in range(2 , 20 , 3): # range(start , stop , step) step mean incresed by 
#        print(n)


# for n in range(1 , 10): 
#        if(n%2 ==0):
#               print(n)

# practice questions 
# num = int(input("enter a number"))
# for n in range(1 , 11):
#     mul = num*n 
#     print(num , "*" , n , "=", mul)
# n = int(input("enter a number"))
# i = 1 
# sum = 0
# while i <= 10: 
#     sum = sum + i 
#     i +=1 
# print(sum)

# n = int(input("enter a number"))
# fact = 1 
# for i in range(1 , n+1):
#     fact = fact * i 
# print(fact)

# n = 5 
# i = 1 
# fact = 1 
# while i <= 5:
#     fact = fact * i
#     i += 1 
# print(fact)

# n = int(input("enter a num"))
# i = 1
# while i <= n: 
#     if(i%2 == 0):
#         print(i)
#     i += 1

# i = 1
# while i < 6:
#     print(i)

#     if(i == 5):
#         break
#     i = i + 1 
for x in range(6):
    if (x == 3):
        break
    print(x)
else:
    print("finished")