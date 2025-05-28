
# take user input as age and check whether user can vote or not and is senior citizen or not


age=(int(input('enter your age:')))

if age<18 :
    print('your age is:',age,' , you cannot vote')
elif age>18 :
    print('your age is:',age,' ,you can vote')
    if age > 70:
        print("and you are sinior citizen")
    else :
        print("and you are not sinior citizen")    
