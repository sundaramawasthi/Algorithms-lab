"""
Experiment 08
Objective: Linear Sort (Counting Sort) for non-negative integers.
Complexity: Best O(n+k), Average O(n+k), Worst O(n+k), Space O(n+k)
"""

arr = list(map(int, input("Enter non-negative integers: ").split()))
n = len(arr)

if n == 0:
    print("Sorted array: []")
else:
    k = max(arr)
    count = [0] * (k + 1)

    for x in arr:
        count[x] += 1

    for i in range(1, k + 1):
        count[i] += count[i - 1]

    output = [0] * n
    for j in range(n - 1, -1, -1):
        count[arr[j]] -= 1
        output[count[arr[j]]] = arr[j]

    print("Sorted array:", output)
