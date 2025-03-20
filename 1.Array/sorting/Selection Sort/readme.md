## **🔷 How Selection Sort Works?**
Selection Sort works by **finding the minimum element** from the unsorted part and swapping it with the first element of that part. This process continues until the array is sorted.

### **🔹 Step-by-Step Walkthrough**
Given:  
`myArray = [4, 3, 5, 1, 3, 4, 9]`

#### **Pass 1 (i = 0)**
- Find the **minimum** in `[4, 3, 5, 1, 3, 4, 9]` → `1`
- Swap `1` with `4`  
**Array after swap:** `[1, 3, 5, 4, 3, 4, 9]`

#### **Pass 2 (i = 1)**
- Find the **minimum** in `[3, 5, 4, 3, 4, 9]` → `3`
- `3` is already in place, so no swap needed  
**Array remains:** `[1, 3, 5, 4, 3, 4, 9]`

#### **Pass 3 (i = 2)**
- Find the **minimum** in `[5, 4, 3, 4, 9]` → `3`
- Swap `3` with `5`  
**Array after swap:** `[1, 3, 3, 4, 5, 4, 9]`

#### **Pass 4 (i = 3)**
- Find the **minimum** in `[4, 5, 4, 9]` → `4`
- `4` is already in place  
**Array remains:** `[1, 3, 3, 4, 5, 4, 9]`

#### **Pass 5 (i = 4)**
- Find the **minimum** in `[5, 4, 9]` → `4`
- Swap `4` with `5`  
**Array after swap:** `[1, 3, 3, 4, 4, 5, 9]`

#### **Pass 6 (i = 5)**
- Find the **minimum** in `[5, 9]` → `5`
- `5` is already in place  
**Array remains:** `[1, 3, 3, 4, 4, 5, 9]`

#### **Pass 7 (i = 6)**
- Only `9` is left, so sorting is complete.

**Final Sorted Array:**  
`[1, 3, 3, 4, 4, 5, 9]` ✅  

---

## **🔷 Time Complexity Analysis**
| Case        | Time Complexity |
|------------|----------------|
| Best Case (Already Sorted) | **O(n²)** |
| Average Case | **O(n²)** |
| Worst Case (Reverse Sorted) | **O(n²)** |

🔹 **Space Complexity:** **O(1)** (Sorting is done in place)  

---

## **🔷Code**
```python
myArray = [4, 3, 5, 1, 3, 4, 9]

length = len(myArray)  # Fixed typo

for i in range(length):
    min_index = i
    for j in range(i + 1, length):
        if myArray[j] < myArray[min_index]:
            min_index = j

    myArray[i], myArray[min_index] = myArray[min_index], myArray[i]  # Swap

print(myArray)
```

---

## **🔷 When to Use Selection Sort?**
✅ Good for small datasets  
✅ Works well when **memory is a constraint**  
❌ Not efficient for large datasets  

