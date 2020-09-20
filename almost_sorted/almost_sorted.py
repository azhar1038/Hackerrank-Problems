def almostSorted(arr):
    peaks=[]
    valleys=[]
    arr.insert(0,0)
    arr.append(1000001)
    for i in range(1, len(arr)-1):
        if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
            valleys.append(i)
        elif arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            peaks.append(i)
    print("Peaks", peaks)
    print("Valleys", valleys)
    if len(valleys) == 0 or len(peaks) == 0:
        print('yes')
    elif len(valleys) > 2 or len(peaks) > 2:
        print('no')
    elif len(valleys) == 1 and len(peaks) == 1:
        v = valleys[0]
        p = peaks[0]
        if arr[v]>arr[p-1] and arr[p]<arr[v+1]:
            print('yes')
            if v-p==1:
                print('swap', p, v)
            else:
                print('reverse', p, v)
        else:
            print('no')
    elif len(valleys) == 2 and len(peaks) == 2:
        p1 = peaks[0]
        p2 = peaks[1]
        v1 = valleys[0]
        v2 = valleys[1]
        if arr[v2]>arr[p1-1] and arr[v2]<arr[p1+1] and arr[p1]<arr[v2+1] and arr[p1]>arr[p2] and v1-p1==1 and v2-p2==1:
            print('yes')
            print('swap', p1, v2)
        else:
            print('no')


almostSorted([1,2,6,4])