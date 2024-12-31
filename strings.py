# to create string 
str = "i am a student"
print(str)
# string length 
print(len(str))
# a letter index in a string 
print(str[3])
# slicing in string 
print(str[0:4])
# negative slicing 
print(str[-3:-1])
# string function 
print(str.endswith("ent"))
print(str.endswith("hjfn"))
print(str.capitalize())
print(str.replace("a" , "pallu"))
print(str.find("a"))
print(str.count("a"))
print(str.find("h"))

# conditionals statements 
# if conditionals 
age = 25 

if(age>=25):
    print("can vote")

# elif conditionals 
name = "palluu"

if(name == "zunnu"):
     print("no")  #indentation is imp 
elif(name == "pallu"):
    print("yes")
else:
    print("yesss")

#  task 
marks = int(input("enter"))

if(marks >= 90 and  marks <= 100):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >=70 and marks < 80):
    grade = "C"
elif(marks < 70 ):
    grade = "D"
print("grade =",grade)

# nesting 
age = 34

if(age >= 18):
    if(age <= 54): 
        print("cannot")
    else:
        print("can drive")
#practice questions
num = int(input("enter"))

if(num%2 == 0):
    print("even")
else:
    print("odd")
