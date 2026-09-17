"""
Experiment 01
Objective: Check whether a given number is prime.
Complexity: Best O(1), Average O(sqrt n), Worst O(sqrt n), Space O(1)
"""

n = int(input("Enter Number: "))

if n <= 1:
    print("Not Prime")
else:
    flag = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            flag = 1
            break
    if flag == 0:
        print("Prime")
    else:
        print("Not Prime")
