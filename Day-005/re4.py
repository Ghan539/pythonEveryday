def prlist(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    prlist(list,idx+1)

fruits=["mango","apple","banana","litchi","pineapple"]    

prlist(fruits)