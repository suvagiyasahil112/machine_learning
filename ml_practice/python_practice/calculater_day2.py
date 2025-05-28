num1=(int(input('enter first number')))
num2=(int(input('enter second number')))

operation=(int(input('enter 1 for addition,2 for substraction,3 for multiplication,4 for division,5 for power\n')))
ops=[1,2,3,4,5]
if operation not in ops:
    print ("enter valid number")
if operation==1:
    print(num1 , "+" , num2 , '=', num1+num2)
if operation==2:
    print(num1 , "-" , num2 , '=', num1-num2)
if operation==3:
    print(num1 , "x" , num2 , '=', num1*num2)
if operation==4:
    print(num1 , "/" , num2 , '=', num1/num2)
if operation==5:
    print(num1 , "to the power of " , num2 , '=', num1**num2)
            
        