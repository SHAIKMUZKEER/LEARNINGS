print(1, 2,3 ,4, 5, 6)
print(1, 2,3 ,4 ,5 ,6 , sep="-")
print(1, 2,3 ,4 ,5 ,6 , sep="\n" , end="*")
print(1, 2,3 ,4 ,5 ,6 , sep="*" , end="\n")

print("i love my{0} and my{1}".format("pallu" , "love")) # curly brackets indicates thst place holder
print("my age is {0} and my{1} ".format(22,12))
print('hello{name} ! {greetings} !'.format(name ="muzkeer" , greetings ="good morning"))
print("i have my own{0} and {1}".format("bread", "bed"))

x = 22.1223
print("the value of x is % 1.4f" %x)

# x = int(input("enter a number :"))
# print(x)
# print(type(x))

# types of errors in python
x = int(input("enter a number"))
y = int(input("enter a number 2"))
z = (x+y)/2
print(z)