list = ["muzkeer" , "pallu" , "majahar" , "momin"]
# print(list)
# print(type(list))
# print(len(list))
# # print(list[1])
# print(list[0])
# list.append("zunnu")
# print(list)
num = [22 , 8 , 28 , 20 , 21]
# num.sort()
# num.sort(reverse=False)
# print(num)
# list.reverse()
# print(list)
# list.insert(3,67)
# print(list)
# num.remove(8)
# print(num)
# list.remove("muzkeer")
# print(list)
# list.pop(2)
# print(list)
# print(list[-3:-1])
# print(list*3)
# print(list[:])
# list.extend(num)
# list.append("zunnu")
# del list[1:3]
# list.count("muzkeer")
# pallu = list.copy()
# print(pallu)
# if "pallu" in list:
#     print("yes")
# list[1:2] = ["zunnu" , "mazza"]
# print(list) 

#  tuples 
# tup = (1 ,2 , 4, 5, 2)
# print(tup)
# print(type(tup))
# print(len(tup))
# print(tup[0:2])
# print(tup.index(5))
# print(tup.count(2))

# diictionary 
# dic = {
#     "name" : "muzkeer",
#     "age" : 26,
#     "marks" : {
#         "phy" : 86,
#         "mat" : 77

#     }
# }
# dic["place"] = "kavali"
# print(dic)
# print(dic["marks"])
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# print(dic.get["name"])
set = {
    1 , 2, 3,4 ,5 
}
set2 = {1 ,2 , 4, 5,6 ,7 ,8 ,8 ,9}
# print(set)
# set.add(26)
# print(set)
# set.remove(26)
# # print(set)
# print(set.union(set2))
# print(set.intersection(set2))
# i = 1 
# while i <= 10:
#     print(i)
#     i = i + 1
# n = int(input("enter a number"))
# i = 1
# while i <= n:
#     if i%2 == 0:
#         print(i)
#     i = i + 1
# i = 1
# while i <= 5:
#     if ( i == 3):
     
#         break
#     print(i)
#     i = i+ 1
# else:
#     print("good bye")
# lists = [1 , 2,3, 4, 5]
# sum = 0
# for n in lists:
#     sum = sum + n 

# n = int(input("enter a number"))
# import random
# rand =  random.choice([1 , 2,3])
# print(rand)
# password = random.randrange(1, n)
# print(password)
# n = int (input("enter"))
# i = 1
# sum = 0
# while i<= n: 
#     if (i%2 != 0):
#        sum = sum + i
#     i = i + 1
# print(sum)
i = 1
c = 0 
n = int(input("enter"))
while i < n+1: 
    if (n %i == 0):
        c = c + 1
    i = i + 1
if(c == 2):
    print("prime")
else:
    print("not")