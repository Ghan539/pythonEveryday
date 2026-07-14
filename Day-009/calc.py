print("calculator")

while True:
    a=int(input("Enter num1 :"))
    b=int(input("Enter num2 :"))

    opt=input("enter operator :")

    if(opt=="+"):
        print("addition : ",a+b)
    elif(opt=="-"):
        print("substract : ",a-b)
    elif(opt=="*"):
        print("multiply : ",a*b)    
    elif(opt=="/"):
        if(b==0):
           print("not possible !!!!")
        else:   
           print("division : ",a/b)  
    elif(opt=="**"):
        print(a,"^",b,"=",a**b)    
    elif(opt=="%"):
        print("remainder : ",a%b)    
    else:
        print("invalid operator")             



    choice=input("do you want to continue ( y or n) :")    

    if(choice.lower()=="n"):
        print("calculator ended")
        break

