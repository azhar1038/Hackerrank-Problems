def activityNotifications(expenditure, d):
    queue = [expenditure[i] for i in range(d)]
    count = 0
    for i in range(d, len(expenditure)):
        sortedQueue = countSort(queue)
        median = sortedQueue[(d-1)//2]
        if d%2 == 0:
            median = (median + sortedQueue[d//2])/2
        if median*2 <= expenditure[i]:
            count += 1
        queue.pop(0)
        queue.append(expenditure[i])
    return count

def countSort(a):
    count = [0 for _ in range(201)]
    for i in a:
        count[i]+=1

    for i in range(1,201):
        count[i] += count[i-1]
    result = [0 for _ in a]
    for i in a:
        result[count[i]-1]=i
        count[i] -= 1
    return result

# print(countSort([5,88,9,80,7]))
print(activityNotifications([10,20,30,40,50], 3))