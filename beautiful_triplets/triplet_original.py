def beautifulTriplets(d, arr):
    count = 0
    for i in arr:
        if i+d in arr and i+2*d in arr:
            count += 1
    return count

arr = [1, 6, 7, 7, 8, 10, 12, 13, 14, 19]
# arr = [1,1,1,2,4,4,4,5,7,7,7,8]
print(beautifulTriplets(3, arr))