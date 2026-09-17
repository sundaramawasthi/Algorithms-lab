"""
Experiment 06
Objective: Sort an array using Insertion Sort.
Complexity: Best O(n), Average O(n^2), Worst O(n^2), Space O(1)
"""

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)

for j in range(1, n):
    key = arr[j]
    i = j - 1
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        i -= 1
    arr[i + 1] = key

print("Sorted array:", arr)
