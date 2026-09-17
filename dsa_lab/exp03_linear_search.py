"""
Experiment 03
Objective: Search an element in a given array using Linear Search.
Complexity: Best O(1), Average O(n), Worst O(n), Space O(1)
"""

arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))
n = len(arr)

pos = -1
for i in range(n):
    if arr[i] == key:
        pos = i
        break

if pos != -1:
    print("Element found at position", pos + 1)
else:
    print("Element not found")
