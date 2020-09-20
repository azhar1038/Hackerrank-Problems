def activityNotifications(expenditure, d):
    queue = [expenditure[i] for i in range(d)]
    count = [0 for _ in range(201)]
    for i in queue:
        count[i]+=1
    alert = 0
    for i in range(d, len(expenditure)):
        median = getMedian(count, d)
        if median*2 <= expenditure[i]:
            alert += 1
        index = queue.pop(0)
        count[index] -= 1
        queue.append(expenditure[i])
        count[expenditure[i]] += 1
    return alert

def getMedian(freq, d):
    count = 0
    if d%2 == 1:
        for i in range(len(freq)):
            count += freq[i]
            if count >= d//2+1:
                return i
    else:
        m1=m2=-1
        for i in range(len(freq)):
            count += freq[i]
            if m1 == -1 and count >= d//2:
                m1 = i
            if count >= d//2+1:
                m2 = i
                break
        return (m1+m2)/2

# print(countSort([5,88,9,80,7]))
print(activityNotifications([10,20,30,40,50], 3))
# print(getMedian([0,2,2],4))