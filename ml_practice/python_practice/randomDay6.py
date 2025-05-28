import random


# for i in range (0,101):
#     a=random.randrange(0,101,2)
#     print(a)

# Suppose you have a bag with 4 red balls, 3 blue balls, and 5 green balls. 
# You randomly draw 2 balls without replacement. 
# What is the probability that:
# 1. Both balls drawn are of the same color.
# 2. At least one ball drawn is green.

# 66 - total 


# bag=["red","red","red","red","blue","blue","blue","green","green","green","green","green"]

# hand=[]
# count =0
# for j in range(0,67): 
#     for i  in range(0,1) :
#         a=random.choice(bag)

#         hand.append(a)
#         bag.remove(a)
#         b=random.choice(bag)
#         hand.append(b)
        

#         if a == b:
#             count+=1

#         bag.append(a)
#         hand.clear()
        

#     print(bag)
#     print(hand)


import random

red_balls = 4
blue_balls = 3
green_balls = 5


total_balls = red_balls + blue_balls + green_balls

num_simulations = 100000  # Number of simulations to run

same_color_count = 0
at_least_one_green_count = 0


for _ in range(num_simulations):
    # Randomly shuffle the balls
    balls = ['red'] * red_balls + ['blue'] * blue_balls + ['green'] * green_balls
    random.shuffle(balls)
    drawn_balls =[]
    drawn_balls.append(balls[:1])
    random.shuffle(balls)
    drawn_balls.append(balls[:1])

    if drawn_balls[0] == drawn_balls[1]:
        same_color_count += 1
    if ['green'] in drawn_balls:
        at_least_one_green_count += 1

print(at_least_one_green_count)
print(same_color_count)
prob_same_color = same_color_count / num_simulations
prob_at_least_one_green = at_least_one_green_count / num_simulations


# Output
print(f"Simulated Probability that both balls are the same color: {prob_same_color:.4f}")
print(f"Simulated Probability that at least one ball is green: {prob_at_least_one_green:.4f}")


