def countInversions(arr):
    n = len(arr)
    inversions = mergeSort(arr, 0, n-1)
    print(arr)
    return inversions

def mergeSort(arr, left, right):
    inversions=0
    if left < right:
        mid = (left+right)//2
        inversions += mergeSort(arr, left, mid)
        inversions += mergeSort(arr, mid+1, right)
        inversions += merge(arr, left, mid, right)
    return inversions

def merge(arr, left, mid, right):
    i = left
    j = mid+1
    k = left
    inversions=0
    sortedArray = [0]*(right+1)
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            sortedArray[k] = arr[i]
            i += 1
            k += 1
        else:
            inversions += mid-i+1
            sortedArray[k] = arr[j]
            j += 1
            k += 1
    
    while i <= mid:
        sortedArray[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        sortedArray[k] = arr[j]
        j += 1
        k += 1

    for index in range(left, right+1):
        arr[index] = sortedArray[index]

    return inversions

print(countInversions([1,5,4,3,2]))