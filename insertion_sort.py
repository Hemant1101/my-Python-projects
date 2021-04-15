def insertion_sort(arr):
    for i in range(1, len(arr)):
        swap = arr[i]
        j = i-1
        while(swap < arr[j] and j >= 0):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = swap
    return arr


l = list(map(int, input("Enter the values: ").split()))
l = insertion_sort(l)
print("Sorted list: ")
for i in l:
    print(i, end=" ")
