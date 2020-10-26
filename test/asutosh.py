SetBalls = [
    "Cosco-Small-58-Red",
    "KC-Medium-95-Red",
    "Stag-Big-156-Red",
    "KC-Medium-95-Red",
    "YSI-Big-152-Red"
]

set_balls = []

for s in SetBalls:
    brand, size, weight, color = s.split("-")
    size_num = 0
    if size == "Medium":
        size_num = 1
    elif size == "Big":
        size_num = 2
    set_balls.append((brand, size_num, int(weight), color))

sort_by = input()
sort_by_index = 0
current = None
if sort_by == "Brand":
    set_balls.sort(key = lambda x: x[0])
    current = set_balls[0][0]
elif sort_by == "Size":
    sort_by_index = 1
    set_balls.sort(key = lambda x: x[1])
    size_num = set_balls[0][1]
    if size_num == 0:
        current = "Small"
    elif size_num == 1:
        current = "Medium"
    elif size_num == 2:
        current = "Big"
elif sort_by == "Weight":
    sort_by_index = 2
    set_balls.sort(key = lambda x: x[2])
    current = set_balls[0][2]
elif sort_by == "Color":
    sort_by_index = 3
    set_balls.sort(key = lambda x: x[3])
    current = set_balls[0][3]

print(current)
for ball in set_balls:
    list_ball = list(ball)
    size = "Small"
    size_num == list_ball[1]
    if size_num == 1:
        size = "Medium"
    elif size_num == 2:
        size = "Big"
    list_ball[1] = size
    if current != list_ball[sort_by_index]:
        print(list_ball[sort_by_index])
        current = list_ball[sort_by_index]
    print("{0}-{1}-{2}-{3}".format(*list_ball))