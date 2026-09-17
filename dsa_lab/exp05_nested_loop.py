"""
Experiment 05
Objective: Complexity of a nested loop.
Complexity: Best O(n^2), Average O(n^2), Worst O(n^2), Space O(1)
"""

n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("Hello")
