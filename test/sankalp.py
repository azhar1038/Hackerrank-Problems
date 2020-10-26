ty=[0,0,0,0,0]
sy=[0,0,0,0,0]
for i in range(10):
    st = input()
    t = st[0:2]
    if t == "TY":
        num = int(st[2:])
        ty[num-1] = num
    elif t =="SY":
        num = int(st[2:])
        sy[num-1] = num

for i in range(5):
    if ty[i] != 0:
        print("[TY0{}]".format(ty[i]), end="")
    else:
        print("[ABSENT]", end="")
    if sy[i] != 0:
        print("[SY0{}]".format(sy[i]), end="")
    else:
        print("[ABSENT]", end="")
    print()