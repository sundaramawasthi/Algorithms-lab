"""
Experiment 07
Objective: Sort an array using Bubble Sort (with early exit).
Complexity: Best O(n), Average O(n^2), Worst O(n^2), Space O(1)
"""

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)

for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break

print("Sorted array:", arr)
