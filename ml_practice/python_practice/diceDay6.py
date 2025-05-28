
# two dice are rolled  50 times, so find probability for :
# 1. second number is adjecent successor of firt number 
# 2. sum of both should be factor of 12 
# 3. sum of both should multiple of 3 and 2

import random

simulation_num=50
fact_of_12=[1,2,3,4,6,12]
multiple_of_3_2=[6,12,18,24,30]

sucessor_count=0
fact_12_count=0
multi_count=0

d1=[1,2,3,4,5,6]
d2=[1,2,3,4,5,6]


for i  in range(simulation_num):
    a=random.choice(d1)
    b=random.choice(d2)

    if b == (a+1) :
        sucessor_count+=1
       
    if a+b in fact_of_12:
        fact_12_count+=1
     

    if a+b in multiple_of_3_2:
        multi_count+=1
       

prob_suc=sucessor_count/simulation_num
prob_fact_12=fact_12_count/simulation_num
prob_multi=multi_count/simulation_num


print(f"PROBABILITY OF SECOND NUMBER BEING ADJCENT SUCCESSOR OF FIRST NUMBER IS:{prob_suc:.4f}")
print(f"PROBABILITY OF SUM OF BOTH NUMBER BEING FACTORIAL OF 12 IS:{prob_fact_12:.4f}")
print(f"PROBABILITY OF SUM OF BOTH NUMBER IS MULTIPLE OF 2 AND 3 IS:{prob_multi:.4f}")



