# import random
# rows=3
# cols=3
# turn=0
# rowlist=[1,2,3]
# collist=[1,2,3]

# def board(cols,rows):
#     for row in range(rows):
#         print("|  " * cols, )


# # board(cols,rows)
# while (turn<11):
#     if turn==0 or 2 or 4 or 6 or 8 or 10:
#         for row in range (rows):
       
#             if row== [random.choice(rowlist)][random.choice(rowlist)  =="|  |  |" ]:                
#                     print("|0" ,"|  " * (cols-1)  )

#                     continue   
#             if row== [random.choice(rowlist)][random.choice(rowlist)  =="|X |  |  " ] or row== [random.choice(rowlist)][random.choice(rowlist)  =="0 |  |  " ] :                
#                     print( "|  |  |" )
                    
#                     continue  
#             print("|  " * cols, )
#         print("\n \n ")
#         turn+=1 


#     if turn==1 or 3 or 5 or 7 or 9 or 11 :
#         for row in range (rows):
       
#             if row== [random.choice(rowlist)][random.choice(rowlist)  =="|  " ]:
                
#                     print("|X |  | "  )
#                     continue   
#             print("|  " * cols, )
#         print("\n \n ")
#         turn+=1 


import random
rows=3
cols=3
turn=5
rowlist=[0,1,2]
collist=[0,1,2]
store1=random.randrange(0,2)
store2=random.randrange(0,2)
def board(cols,rows):
    for row in range(rows):
        print("|  " *cols )


board(cols,rows)


blank="| "
prnx="|X "
prn0="|0 "
# list=blank,prnx,prn0



while turn<20 :
    if turn%2 != 0:
        for row in range (rows*cols):
            if row == [store1][store2]  :
                print(blank,prn0,blank)
        turn+=1



    if turn%2 == 0:
        for row in range (rows*cols):
            if row ==[store1][store2]   :
                print(blank,prnx,blank)
        turn+=1









# new late night

# random.choice(rowlist)][random.choice(rowlist)
# random.choice(rowlist)][random.choice(rowlist)        






# print("\nrandomlist",randomlist , "\n")
# print("\nstructure of tic")



# for row in range (rows):
#     if row == [random.randrange(0,3)][random.randrange(0,1)] =="|  ":
#         tic[row]= j
#         print(tic)