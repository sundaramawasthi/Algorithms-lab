"""
Experiment 09
Objective: Sort an array using Selection Sort.
Complexity: Best O(n^2), Average O(n^2), Worst O(n^2), Space O(1)
"""

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("Sorted array:", arr)
