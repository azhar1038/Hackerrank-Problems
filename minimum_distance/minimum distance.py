def minimumDistances(a):
    min_distance = len(a)
    nums = {}
    for i in range(len(a)):
        try:
            distance = i - nums[a[i]]
            if distance < min_distance:
                min_distance = distance
            nums[a[i]] = i

        except:
            nums[a[i]] = i
    print(nums)
    if min_distance == len(a):
        min_distance = -1
    print(min_distance)

minimumDistances([1,2,3,4,5,67,7])
