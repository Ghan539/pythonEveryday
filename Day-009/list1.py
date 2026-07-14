l=[11,24,34,54,75,54,543]

t=len(l)
print(t)


for i in range(t-1 ,-1,-1):
    print(l[i],end=" ")

for i in range(-1 ,-t-1,-1):
    print(l[i],end=" ")    

print()

for i in l:
    print(i,end=" ")

print()

for i in range(t):
    print(l[i],end=" ")