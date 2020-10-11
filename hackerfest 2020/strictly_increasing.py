from collections import defaultdict
def whoIsTheWinner(arr):
    d=defaultdict(lambda: False)
    repeat=False
    for i in arr:
        if not d[i]:
            d[i]=True
        else:
            repeat=True
            break
    if not repeat:
        return "First"
    if len(arr)%2==0:
        return "Second"
    return "First"

for _ in range(int(input())):
    input()
    print(whoIsTheWinner(list(map(int, input().split()))))