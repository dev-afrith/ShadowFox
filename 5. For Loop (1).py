print("\t\t5. For Loop")


'''1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20
times).
Count and print the following statistics:
How many times you rolled a 6
How many times you rolled a 1
How many times you rolled two 6s in a row'''

"""In this program i have used a random library and uses the variable to store a initial value,
after that a for loop for looping it for 20 times , a using the logic for the program , at last printed
the values of the results"""

import random

rolling_die = 20     #for 20 times 
count_of_6_rolles = 0
count_of_1_rolles = 0
count_of_6_doubled = 0
previously_rolled = 0

for i in range(rolling_die):
    roll = random.randint(1, 6)  # random number b/w 1 to 6
    print(f"Roll {i + 1}: {roll}")

    if roll == 6:
        count_of_6_rolles += 1
        if previously_rolled == 6:
            count_of_6_doubled += 1
    if roll == 1:
        count_of_1_rolles += 1

previously_rolled = roll  


print("\n")

print("Results: ")
print(f" No of times rolled a 6: {count_of_6_rolles}")
print(f" No of times rolled a 1: {count_of_1_rolles}")
print(f" No of times two 6s rolled in a row: {count_of_6_doubled}")
