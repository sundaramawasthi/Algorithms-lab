"""
Experiment 10
Objective: Print a right-angled multiplication triangle for a positive integer n.
Complexity: Best O(n^2), Average O(n^2), Worst O(n^2), Space O(1)
"""

n = int(input("Enter a positive integer: "))

if n > 10:
    print("This might take a while...")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()
