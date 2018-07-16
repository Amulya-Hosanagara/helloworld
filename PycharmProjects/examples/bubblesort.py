import os
def Sorting(arr):
    size = len(arr)

    for i in range(size):
        for j in range(0, size-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#arr = [20,34,15,16,89]


arr = input("enter the array element to sort: ").split(",")

Sorting(arr)

print("sorted bubble sort array: ")
for i in range(len(arr)):
    print(arr[i])
