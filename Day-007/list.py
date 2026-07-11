movies=[]
movies.append(input("enter m1 : "))
movies.append(input("enter m2 : "))
movies.append(input("enter m3 : "))
print(movies)



list=["m","a","a","m"]
clist=list.copy()
clist.reverse()
if(list==clist):
    print("palindrome")
else:
    print("not palindrome")