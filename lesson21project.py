# Conditional Probability

red_balls = 1
blue_balls = 6
white_balls = 3

total_balls = red_balls + blue_balls + white_balls

# Given that the first ball was white,
# and it is replaced, the basket stays the same.
probability_second_white = white_balls / total_balls

print("Total balls:", total_balls)
print("White balls:", white_balls)

print(
    "Probability that the second ball is white given "
    "the first ball was white:",
    probability_second_white
)

print("Probability as a percentage:",
      probability_second_white * 100, "%")