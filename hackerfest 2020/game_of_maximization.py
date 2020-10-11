def maximumStones(arr):
    odd_sum = even_sum = 0
    for i,a in enumerate(arr):
        if i%2==0:
            even_sum+=a
        else:
            odd_sum+=a
    return 2*min(odd_sum, even_sum)

input()
arr=list(map(int, input().split()))
print(maximumStones(arr))