# f = open("pallu.txt" ,  "r")
# dat = f.read()
# data = f.readline()

# data2 = f.readline()
# print(dat)
# print(data)
# print(data2)
# f.close()
# f = open("modelsuresh.txt" ,"a")
# date = f.write("\n pallu is my bestie ")
# print(date)
# f.close()

with open("practice1.txt" , "r") as f:
    data = f.read()

datenew = data.replace("Java" , "python")
print(datenew)

with open("practice1.txt" , "w") as f:
    f.write(datenew)
