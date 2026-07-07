num=int(input("enter num : "))

def sum(n):
    if(n==1):
      return 1
    else:
       return n+(n-1)
    
z=sum(num)
print("the sum of first",num,"natural no is : ",z)