#q1
game_name  ="Dark Souls"
dob=2011
time=6.7
is_game_fun = True

print(type(game_name))
print(type(dob))
print(type(time))
print(type(is_game_fun))

# q2
age = int(input("Enter your age: "))
print("Next year u will be ", age+1)

#q3
height = float(input("Enter your height in meters: "))
print("Your height in cm is ", height * 100, "cm")


#q4
marks = input("Enter your marks: ")
print(int(marks))

#q5
clg ="Graphic Era Hill University"
print(clg.upper())
print(clg.lower())
print("Length:",len(clg))


#q6
price =float(input("Enter your price: "))
quantity = int(input("Enter your quantity: "))
total_bill = price * quantity
print("Total bill is :",total_bill)
print(type(total_bill))

#q7
is_student = True
have_laptop = False
can_study = is_student and have_laptop
print(can_study)


#q8
name ="Subhanshu"
age = 19
height = 1.9
print("my name is ",name,". I am ",age,"years old and my height is",height,".")

#q9
height=1.9
height2=int(1.9)
print(height ,height2)

#q10
list=[1,2,3,4,5]
for i in list:
    print(i , type(i))