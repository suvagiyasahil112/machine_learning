import random
rows=3
cols=3
turn=0
zero="|O "
eks="|X "

def board(cols,rows):
    for row in range(rows):
        
        print("| "  * cols)
       
    
board(cols,rows)



while (turn<=9):
    if turn%2 !=0:
        for row in range (rows*cols):
       
            if row== [random.randrange(0,3)][random.randrange(0,1)]:                
                print("|O |  | "   )
                continue   
            print("|  " * cols, )
        print("\n \n ")
        turn+=1 

    if turn==0 or 2 or 4 or 6 or 8 :
            for row in range (rows):
                
                if  row=="|  ":
                    print("*")
                    if  row ==[random.randrange(0,3)][random.randrange(0,3)] == str("|  ") :
                        print("|X" ,"|  " * (cols-1)  )
                        continue 
                print("|  " * cols, )
            print("\n \n ")
            turn+=1      
    if turn%2 ==0:
        for row in range (rows*cols):
       
            if row== [random.randrange(0,3)][random.randrange(0,3)]:
                if row == [0][0]:

                    print("|X |  | "  )
                    continue   
            print("|  " * cols, )
        print("\n \n ")
        turn+=1 





# for row in range(rows):
#     if row == [0][0]:
#         print("|X" ,"|  " * (cols-1)  )
#         continue
#     if row ==[1][0]:
#         print("|0" ,"|  " * (cols-1)  )
#         continue   
#     print("|  " * cols, )


# # ########################################for 111
                  



# # a ="gyy"

# # print("o" , a.join("huuu"))



