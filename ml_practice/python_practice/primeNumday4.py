# give prime numbers between range 

start=int((input('enter starting point')))
end=int((input('enter ending point')))

def check_prime(start,end):
    for i in range (start,end+1):
        if i>1 :
            for j in range (2,i):
                if i%j==0:
                    break
            else :
                print(i)
    return i
check_prime(start,end)


