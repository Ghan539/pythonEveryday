a=int(input("Enter num1 : "))
b=int(input("Enter num2 : "))

print("before swap : ",a,b)

a=a+b
b=a-b
a=a-b

print("after swap : ",a,b)