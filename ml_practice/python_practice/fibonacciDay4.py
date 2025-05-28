

# def fib(t1,t2,add,num,n):
#     if n<=0:
#         print('enter positive and non zero number')

#     else:    
#         while num<n:
            
#             print(t1)
#             nth=t1+t2
#             t1=t2
#             t2=nth
#             num=num+1
        

# # first two terms 0 ,1 
# t1=0
# t2=1
# add=0
# num=0

# n=(int(input('enter how many terms of fibonacci to print:')))
# fib(t1,t2,add,num,n)

# Python Program to find the L.C.M. of two input number

def compute_lcm(num1,num2):

   # choose the greater number
   if num1 > num2:
       greater = num1
   else:
       greater = num2

   while(True):
       if((greater % num1 == 0) and (greater % num2 == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))