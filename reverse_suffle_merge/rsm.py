from collections import Counter

def isBetter(a, stack):
    if len(stack) == 0 or a < stack[-1]:
        return True
    return False

def isNeeded(a, needed, used):
    if needed[a] > 0:
        needed[a] -= 1
        return True
    return False

def canPop(needed, used, total, stack):
    if len(stack) == 0:
        return False
    a = stack[-1]
    if needed[a]+1 <= total[a]-used[a]:
        needed[a] += 1
        return True
    return False

def reverseShuffleMerge(s):
    total = Counter(s)
    needed = Counter()
    used = Counter()
    stack = []
    for key in total:
        needed[key] = total[key]//2
    for c in reversed(s):
        if isNeeded(c, needed, used):
            while isBetter(c, stack) and canPop(needed, used, total, stack):
                stack.pop(-1)
            stack.append(c)
        used[c] += 1
    # print("NEEDED",needed)
    # print("USED", used)
    # print("STACK", stack)
    # print("\n")
    # print(total)
    return "".join(stack)

print(reverseShuffleMerge("abcdefgabcdefg"))