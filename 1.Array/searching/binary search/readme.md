### **Python Code with Step-by-Step Visualization**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    print(f"Initial Array: {arr}")
    print(f"Target: {target}")
    print("----------------------------")

    while left <= right:
        mid = left + (right - left) // 2

        # Visualization
        print(f"Left: {left}, Right: {right}, Mid: {mid}")
        print(f"Checking: arr[{mid}] = {arr[mid]}")

        if arr[mid] == target:
            print(f"Target found at index: {mid}")
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

        print(f"Updated Left: {left}, Updated Right: {right}")
        print("----------------------------")

    print("Target not found in the array.")
    return -1  # Target not found

# Example usage
sorted_array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
target = 23
binary_search(sorted_array, target)

```

---

### **Explanation & Visualization Example**
For the sorted array:  
`[2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]`  
If the **target = 23**, the search progresses as follows:

| Iteration | Left | Right | Mid | arr[mid] | Comparison |
|-----------|------|-------|-----|---------|------------|
| 1st       | 0    | 10    | 5   | 23      | Found ✅   |

Since `arr[5] = 23`, the search stops immediately.

If the **target = 16**, the search progresses like this:

| Iteration | Left | Right | Mid | arr[mid] | Comparison |
|-----------|------|-------|-----|---------|------------|
| 1st       | 0    | 10    | 5   | 23      | Search Left |
| 2nd       | 0    | 4     | 2   | 8       | Search Right |
| 3rd       | 3    | 4     | 3   | 12      | Search Right |
| 4th       | 4    | 4     | 4   | 16      | Found ✅   |

---

### **Key Points**
✅ **Time Complexity:** `O(log n)`  
✅ **Space Complexity:** `O(1)` (Iterative approach, no extra space)  
✅ **Works only on sorted arrays**  
