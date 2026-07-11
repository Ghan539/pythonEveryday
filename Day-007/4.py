num=int(input("enter number: "))
if(num%2==0):
    print("even")
else:
    print("odd")


a=int(input("enter first number: "))    
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if(a>=b and a>=c):
    print("largest is ",a)
elif(b>=a and b>=c):
    print("largest is ",b)
else:
    print("largest is ",c)



num=float(input("enter number: "))
if(num%7==0):
    print("divisible by 7")
else:
    print("not divisible by 7")