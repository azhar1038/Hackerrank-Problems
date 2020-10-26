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

if sort_by == "Brand":
    set_balls.sort(key = lambda x: x[0])
    print(set_balls[0][0])
elif sort_by == "Size":
    set_balls.sort(key = lambda x: x[1])
    size_num = set_balls[0][1]
    if size_num == 0:
        print("Small")
    elif size_num == 1:
        print("Medium")
    elif size_num == 2:
        print("Big")
elif sort_by == "Weight":
    set_balls.sort(key = lambda x: x[2])
    print(set_balls[0][2])
elif sort_by == "Color":
    set_balls.sort(key = lambda x: x[3])
    print(set_balls[0][3])

for ball in set_balls:
    brand, size_num, weight, color = ball
    size = "Small"
    if size_num == 1:
        size = "Medium"
    elif size_num == 2:
        size = "Big"
    print("{0}-{1}-{2}-{3}".format(brand, size, str(weight), color))