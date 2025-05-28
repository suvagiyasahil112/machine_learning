# A family has three children. What is the probability that all three children are boys, 
# assuming the probability of having a boy or girl is equal?
import random
simulation_num=100000
all_boys_count=0

sample_space=['boy','girl']

for i in range (simulation_num):
    children=[]
    for j in range(0,3):
        
        random.shuffle(sample_space)
        children.append(sample_space[:1])

    if children[0]==children[1]==children[2]==['boy']:
        all_boys_count+=1

prob=all_boys_count/simulation_num
print(f"PROBABILITY:{prob:.4f}")