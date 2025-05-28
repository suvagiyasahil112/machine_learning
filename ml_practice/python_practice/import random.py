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
    drawn_balls = balls[:2]

    if drawn_balls[0] == drawn_balls[1]:
        same_color_count += 1
    if 'green' in drawn_balls:
        at_least_one_green_count += 1

prob_same_color = same_color_count / num_simulations
prob_at_least_one_green = at_least_one_green_count / num_simulations


# Output
print(f"Simulated Probability that both balls are the same color: {prob_same_color:.4f}")
print(f"Simulated Probability that at least one ball is green: {prob_at_least_one_green:.4f}")








