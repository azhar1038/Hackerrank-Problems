from collections import defaultdict
def countTriplets(arr, r):
    right=defaultdict(lambda: 0)
    for i in arr:
        right[i] += 1
    left=defaultdict(lambda: 0)
    count=0
    for j in arr:
        i = j//r
        k = j*r
        right[j] -= 1
        if left[i] and right[k] and not j%r:
            count += left[i]*right[k]
        left[j] += 1
    return count

print(countTriplets([2,2,3,6,4,8,12], 2))