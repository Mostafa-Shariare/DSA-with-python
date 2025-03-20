myArray = [4,3,5,1,3,4,9]

length = len(myArray)

for i in range(length):
    min_index = i
    for j in range(i+1, length):
        if myArray[j] < myArray[min_index]:
            min_index = j

    myArray[i], myArray[min_index] = myArray[min_index], myArray[i]

print(myArray)




