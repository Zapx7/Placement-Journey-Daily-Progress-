#q 1
def add(a,b):
    return a+b

#q2
def helloName(a):
    print(f"Hello!! {a} , Welcome to the Grind!!")
a=input("enter your name ")
helloName(a)

#q3
def add(a=1,b=2):
    return a+b

add()

#q4
def evenODD(a):
    if  a%2==0:
        print(f"Even")
    else:
        print(f"Odd")

a=int(input("Enter a number :"))
evenODD(a)

#q5
def lst_add(a):
    x=0
    for i in a:
        x=x+i
    return x
a=[1,2,3,4,5]
lst_add(a)
print(lst_add(a))

#q6
def result(a):
    if a > 40:
        return "Pass"
    else:
        return "Fail"

a=int(input("Enter your marks :"))
result(a)
print(result(a))
#q7
def comp(a,b):
    return f"My name is {a} and I am {b} years old ."
a=input("Enter your name:")
b=int(input("Enter your age:"))
print(comp(a,b))

#q8
def average(a,b,c):
    return (a+b+c)/3
a=int(input ( f"Enter a number:"))
b=int(input ( f"Enter a number:"))
c=int(input ( f"Enter a number:"))
print(average(a,b,c))