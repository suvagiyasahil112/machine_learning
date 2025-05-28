print("hello")
import random
turn=0
i= "|  "
j="|O "
k="|X "
tic=[["|  "]*3,["|  "]*3,["|  "]*3]

def structure(tic):
    for i in  tic :
        print(i, "\n")

structure(tic)
# randnumber = random.randint(0,9)
# tic.pop(randnumber)
# tic.insert("|O",randnumber)

randomlist=[]
ii=0
jj=0
for ii in range(0,3) :
    for jj in range (0,3):
        # print(ii,jj)
        randomlist.append([[ii],[jj]])
        
    
while (turn<=9):
    if turn%2 != 0:
        
        flag=True
        while (flag == True):
            flag2=0
            randnumber1=0
            randnumber2=0
            # print(randnumber)
            while (flag2 == 0 ):
                if tic[random.randrange(0,3)][random.randrange(0,3)]=="|  ":
                    
                    tic.pop([randnumber1][randnumber2])
                    tic.insert([randnumber1][randnumber2],"|O ")
                    flag2=1

            flag=False
        turn+=1



    if turn%2 == 0:
        
        flag=True
        while (flag == True):
            flag2=0
            print("tic",tic)
            randnumber1=random.randint(0,2)
            randnumber2=random.randint(0,2)
            print(randnumber1)
            print(randnumber2)
            while (flag2 == 0 ):
                if tic[randnumber1][randnumber2]=="|  ":
                    tic.pop([randnumber1][randnumber2])
                    tic.insert([randnumber1][randnumber2],"|X ")
                    print("jyagsbcd")
                    flag2=1
                    continue

            flag=False
               
                # structure(tic)
                

        turn+=1

structure(tic)

# e=randomlist
# print(e)
# a=random.choice(randomlist)
# print(a)
# returns [0][1]
# a=randomlist[0][1]
# print(a)
# randnumber1 = random.randrange(0,3)
# randnumber2 = random.randrange(0,3)

# x=(tic([randnumber1][randnumber2]))
# print(x)

# print(tic[random.randrange(0,3)][random.randrange(0,3)])

# if tic[randnumber1][randnumber2]=="|  ":
#     print([randnumber1][randnumber2])


# s=random.choice(randomlist)
# print(s)

# randnumber =random.choice(randomlist)
# if tic [randnumber]== "|  ":
#     print("pass")



