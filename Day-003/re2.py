num=int(input("enter positive num :"))

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)


fact=factorial(num)
print("the factorial of",num,"is : ",fact)