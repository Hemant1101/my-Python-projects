def findMinAndMax(A, left, right, min, max):
    if left == right:
        if min > A[right]:
            min = A[right]
        if max < A[left]:
            max = A[left]
        return min, max

    if right - left == 1:
        if A[left] < A[right]:
            if min > A[left]:
                min = A[left]
            if max < A[right]:
                max = A[right]
        else:
            if min > A[right]:
                min = A[right]
            if max < A[left]:
                max = A[left]
        return min, max

    mid = (left + right) // 2
    min, max = findMinAndMax(A, left, mid, min, max)
    min, max = findMinAndMax(A, mid + 1, right, min, max)
    return min, max


INF = 99999

arr = list(map(int, input("Enter the array: ").split()))

(min, max) = (INF, -INF)
(min, max) = findMinAndMax(arr, 0, len(arr) - 1, min, max)

print("The minimum element in the list is", min)
print("The maximum element in the list is", max)
