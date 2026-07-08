tup=(1,4,9,16,25,36,49,64,81,100)
print(tup)
x=int(input("enter number from tup:"))
i=0
while i<len(tup):
    if tup[i]==x:
        print("number found at index :",i)
        break
    i=i+1
