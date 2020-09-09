class Item:
    def __init__(self, value, repeat):
        self.value = value
        self.repeat = repeat
    def __str__(self):
        return f"({self.value}, {self.repeat})"

def beautifulTriplets(d, arr):
    m_arr = []
    i=0
    while i < len(arr):
        j=i
        repeat=0
        while arr[i] == arr[j]:
            repeat += 1
            j += 1
            if j == len(arr):
                break
        i = j
        item = Item(arr[i-1], repeat)
        m_arr.append(item)
    count = 0
    for i in range(0, len(m_arr)):
        index_d=index_2d = -1
        for j in range(i+1, len(m_arr)):
            if m_arr[i].value + d == m_arr[j].value:
                index_d = j
            elif m_arr[i].value + 2*d == m_arr[j].value:
                index_2d = j
        if index_d > 0 and index_2d > 0:
            count += m_arr[i].repeat * m_arr[index_d].repeat * m_arr[index_2d].repeat
    return count

arr = [1, 6, 7, 7, 8, 10, 12, 13, 14, 19]
# arr = [1,1,1,2,4,4,4,5,7,7,7,8]
print(beautifulTriplets(3, arr))