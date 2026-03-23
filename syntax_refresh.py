#variable and datatypes
name ="Subhanshu"   #string
age =  19           #int
height= 5.9         #float
is_student =True    #boolean

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#inpt +Type conversion
marks = input("Enter Marks: ")
marks= int(marks)
print("Marks : ",marks)

height_str = 5.9
height = float(height_str)
print(height)
print(height_str)

#string
clg ="Graphic Era Hill Universty"
print(clg.upper())
print(len(clg))

#lists
fruits=["apple","banana"]
fruits.append("mango")
print(fruits)

#for loof & if
for i in fruits:
    if len(i) > 5:
        print(i,"is long ")
    else:
        print(i,"is short")