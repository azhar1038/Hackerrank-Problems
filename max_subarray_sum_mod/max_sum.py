def maximumSum(a, m):
    cumulative = [(0,a[0]%m)]
    for i in range(1, len(a)):
        cumulative.append((i, (a[i]+cumulative[i-1][1])%m))
    cumulative.sort(key=lambda c: c[1])
    minimum = m+1
    maximum=0
    for i in range(0, len(cumulative)-1):
        diff = cumulative[i+1][1] - cumulative[i][1]
        indexDiff = cumulative[i][0] - cumulative[i+1][0]
        if indexDiff > 0 and diff < minimum:
            minimum = diff
            maximum = m - diff
    return max(maximum, cumulative[-1][1])

    # prefix=0
    # maximum=0
    # s = set()
    # s.add(0)
    # for i in range(len(a)):
    #     prefix = (prefix+a[i])%m
    #     maximum = max(maximum, prefix)
    #     it=0
    #     for i in s:
    #         if i >= prefix+1:
    #             it=i
    #     if it != 0:
    #         maximum = max(maximum, prefix-it+m)
    #     s.add(prefix)
    # return maximum
    

print(maximumSum([5,5,5,5,5],5))