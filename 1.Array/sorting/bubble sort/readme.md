## 🔷 **Bubble Sort Explanation**  
Bubble Sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order. This process continues until the entire array is sorted.

### **🔹 How Bubble Sort Works?**
- Compare adjacent elements and swap if the left element is greater than the right.
- Move the largest element to the end in each iteration.
- Repeat this process for the remaining unsorted elements.

---

## 🔷 **Step-by-Step Walkthrough with Your Code**
**Initial Array:** `[2, 4, 5, 1, 3, 5]`

### **🔹 Pass 1**
- Compare `2` and `4` → No swap  
- Compare `4` and `5` → No swap  
- Compare `5` and `1` → Swap `[2, 4, 1, 5, 3, 5]`  
- Compare `5` and `3` → Swap `[2, 4, 1, 3, 5, 5]`  
- Compare `5` and `5` → No swap  

**After Pass 1:** `[2, 4, 1, 3, 5, 5]`

---

### **🔹 Pass 2**
- Compare `2` and `4` → No swap  
- Compare `4` and `1` → Swap `[2, 1, 4, 3, 5, 5]`  
- Compare `4` and `3` → Swap `[2, 1, 3, 4, 5, 5]`  
- Compare `4` and `5` → No swap  

**After Pass 2:** `[2, 1, 3, 4, 5, 5]`

---

### **🔹 Pass 3**
- Compare `2` and `1` → Swap `[1, 2, 3, 4, 5, 5]`  
- Compare `2` and `3` → No swap  
- Compare `3` and `4` → No swap  

**After Pass 3:** `[1, 2, 3, 4, 5, 5]`

---

### **🔹 Pass 4**
- Compare `1` and `2` → No swap  
- Compare `2` and `3` → No swap  

**Array is now sorted! 🎉**  

---

## 🔷 **Visual Representation**
Here's a step-by-step visual representation of how Bubble Sort works on your array:

```
Pass 1:  [2, 4, 5, 1, 3, 5]  
          [2, 4, 1, 5, 3, 5]  (Swap 5 and 1)
          [2, 4, 1, 3, 5, 5]  (Swap 5 and 3)

Pass 2:  [2, 1, 4, 3, 5, 5]  (Swap 4 and 1)
          [2, 1, 3, 4, 5, 5]  (Swap 4 and 3)

Pass 3:  [1, 2, 3, 4, 5, 5]  (Swap 2 and 1)
```
The final sorted array is: `[1, 2, 3, 4, 5, 5]`

---

## 🔷 **Time Complexity Analysis**
| Case        | Complexity |
|------------|-----------|
| Best Case (Already Sorted) | **O(n)** |
| Average Case | **O(n²)** |
| Worst Case (Reverse Sorted) | **O(n²)** |

### **🔹 Space Complexity**
- **O(1)** (No extra space needed; sorting is done in-place)

---

## 🔷 **When to Use Bubble Sort?**
✅ **Good for learning basic sorting concepts**  
✅ **Works well for small arrays**  
❌ **Not efficient for large datasets**  

### **🔹 Optimization**
A small improvement can be made by adding a **flag** to check if any swaps were made in a pass. If no swaps were made, the array is already sorted, and we can **break early** to improve efficiency.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # Optimization flag
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # A swap occurred
        if not swapped:  # If no swaps, the array is already sorted
            break

arr = [2, 4, 5, 1, 3, 5]
bubble_sort(arr)
print("Sorted array:", arr)
```

**Time Complexity (Optimized)**
- Best Case: **O(n)**
- Worst/Average Case: **O(n²)**

