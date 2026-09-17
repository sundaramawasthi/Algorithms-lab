"""
Experiment 02
Objective: Find the maximum and minimum of a given array.
Complexity: Best O(n), Average O(n), Worst O(n), Space O(1)
"""

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)

maximum = arr[0]
minimum = arr[0]

for i in range(1, n):
    if arr[i] > maximum:
        maximum = arr[i]
    if arr[i] < minimum:
        minimum = arr[i]

print("Maximum:", maximum)
print("Minimum:", minimum)
