list=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter x: "))
idx=0
for el in list:
 if(el==x):
  print("num found at idx:",idx)
  idx=idx+1
  break
   