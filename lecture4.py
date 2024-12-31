# dictionary 
# about = {
#     "name " : "muzkeer",
#     "subject" : ["python","java"],
#     "topic" : ("dictionary"),
#     "age" : 25, 
#     25 : True,
# } 
# about["name"] = "pallu"
# print(about)
#  nesting in dictionaries 
# student = {
#     "name" : "muzkeer",
#     "marks" : {
#         "mat" : 100,
#         "phy" : 99,
#     }
# }
# print(student["marks"]["mat"])
# methods of dictionaries 
# about = {
#     "name " : "muzkeer",
#     "subject" : ["python","java"],
#     "topic" : ("dictionary"),
#     "age" : 25, 
#     25 : True,
# } 
# print(about.keys())
# print(len(about)) # gives the dictionary length
# print(list(about.keys())) #convert the all key in dictionaries in list
# print(about.values()) 
# print(list(about.values()))  #convert the all values in dictionaries in list 
# print(about.items()) #gives the value in tuples 
# print(about.get("topic")) # give the value of key in dictionary 
# about.update({"place" : "delhi"}) # insert a specific items to dictionary 
# print(about)


# sets in py
# items = {
#     1,2,3,5,6,7,7,7
# }
# print(items)
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("muzkeer")
# collection.add(1)
# collection.clear()
# collection.remove(2)
# print(collection.pop())
# print(collection.pop())
# set1 = {1 , 2, 3}
# set2 = {4 , 2, 3, 5}
# print(set1.union(set2))
# print(set1.intersection(set2))
# practice questions 
# dict = {
#     "table" : ["a piece" ,"fact"], 
#     "cat"   : "a small animal"
# }
# print(dict)

# set = {"python" , "java" , "c++", "python" , "javascript" , "java" , "python" , "java" , "c++" , "c"}
# print(len(set))
dict = {}

x = int(input("enter a number"))

dict.update({"math" : x})
y = int(input("enter a number"))
dict.update({"phy" : y})
z = int(input("enter a number"))
dict.update({"chem" : z})
print(dict)


