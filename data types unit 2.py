# numerical data type  -> int , float , complex 
a = 10 
print(type(a))
b = 2.8
print(type(b))
c = 10j
print(type(credits))
print(a,isinstance(a,int))
print(b , isinstance(b,float))
print(c , isinstance(c,complex))

# squcence type -> str , list , tuple , range 

d = "muzkeer"
print(type(d))

list = ["muzkeer" ,1 , 2,3 ,4]
list.append("zunnu")
print(list)
list[1] = "pallu"
print(list)
list.remove("muzkeer")
print(list)
print(list.pop(1))

tup = (1 , 2,3 ,4 ,5)
print(type(tup))


for a in range(0 ,11):
    print(a)
# mapping data type  dictionary , sets 
dict = {
    "name" : "muzkeer",
    "age" : 36
}
print(dict)
dict["name"] = "pallu"
print(dict.items())
print(dict.keys())
print(dict.values())
print(dict.get("name"))
dict.update({"palce" : "kavali"})
print(dict)



set = {1, 2, 3, 4, 4}
print(set)

str = "muzkeer"
print(str[1:4])







