#Implementation of Bubble Sort

def bubblesort(arr):
    n=len(arr)
    swapped=False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                swapped=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    if not swapped:
        return

# Driver code for test
arr=[29,12,4,56,8,5]
bubblesort(arr)

# Sorted array print
print("Sorted array is:")
for i in range(len(arr)):
    print("%d"%arr[i],end=" ")
