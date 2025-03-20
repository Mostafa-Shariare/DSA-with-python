myArray = [2,4,5,1,3,5]

n = len(myArray)

for i in range(n-1):
    for j in range(n-i-1):
        if myArray[j] > myArray[j+1]:
            myArray[j], myArray[j+1] = myArray[j+1], myArray[j]

print(myArray)
