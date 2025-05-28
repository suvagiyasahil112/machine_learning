

def  factfunc(num):

    if num<0 :
        print("enter positive number")
    fact=1    
    
    for i in range (1,num+1):
        fact=fact*i
        
    print(fact)

num=int(input('enter number:'))
ans=factfunc(num)