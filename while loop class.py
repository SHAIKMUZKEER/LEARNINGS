# n = int(input("enter a name"))
# i = 1
# while i <= n:
#     if i %2 == 0:
#         print(i)
#     i = i +1 
# ## prime 
# for i in range(2 , 20):
#     for j in range(2 , i):
#         if(i%j == 0):
#             break
#     else:
#         print(i)

# i = 1 
# while i <= 6:
#     print(i)
#     i = i +1 
# else:
#     print("loop is successfully completed")

# i = 1
# while i <= 6:
#     if (i == 5):
#         break
#     print(i)
#     i = i + 1
# else:
#     print("good morning")

# sum = 0
# list = [1 , 2, 3, 4, 5, 6 ,7]
# for i in list:
#     sum = sum + i
# print(sum)

# n = int(input("enter a number"))
# for i in range(1 , n +1 , 1):
#     print(i)


# for i in range(1 , 10):
#     for j in range(0, i):
#         print("sunny" , end = " ")
#     print

# for i in range(1 , 11):
#     if (i == 6 ):
#         break
#     print(i)
# else:
#     print("hello")

## nested loop
# n = int(input("enter a number"))
# for i in range(1 , n+1):
#     for j in range(i):
#         print("*" , end = " ")
#     print()

## foe while loopm
# n = int(input("enter a number"))
# i = 1
# while i <= n: 
#     j = 1
#     while j <= i:
#         print("*" , end = " ")
#         j = j + 1 
#     print()
#     i = i + 1

# n = int(input("enter a number"))
# for i in range(1 , n + 1):
#     j = 1 
#     while j<= i:
#         print("*", end = " ")
#         j = j + 1 
#     print()


# n = int(input("enter a number"))
# i = 1 
# while i <= n:
#     for j in range(i):
#         print("*" , end =" ")
#     print()
#     i = i + 1 

# n = int(input("enter a number"))
# i = n
# while i>=1:
#     print(i)
#     i = i - 1 

# n = int(input("enter a number"))
# for i in range( n , 0, -1):
#     print(i)
# a = int(input("enter a number"))
# for i in a:
#     for j in i:
#         print("muzkeer", end=" ")
#     print()

# for i in range(1 , 10 , 2):
#     j = i 
#     while j <= i:
#         if(j%2 == 0):

# i = 65
# size = 7
# for i in range(0 , size):
#     for j in range(0, i+1):
#         character = chr(i)
#         print(character , end = " ")
#         i = i + 1 
#     print(" PYTHON")

# for i in range(0 , 21):
#     if i%2 == 0:
#         print("even" , i)
#     else:
#         print("odd" , i)

a = input("enter a number")
size = len(a)
for i in range(0 , size):
    for j in range(0 , i + 1 ):
        print(a[j] , end = " ")
    print()