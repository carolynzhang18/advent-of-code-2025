fresh = []
available = []
nxt = False
with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip('\n')
        if line == "":
            nxt = True
            continue
        if not nxt:
            fresh.append(list(map(lambda x: int(x), line.split("-"))))
        else:
            available.append(int(line))

fresh.sort()
available.sort()

def solution1():
    curr_range = 0
    ans = 0
    for ing in available:
        if ing < fresh[curr_range][0]:
            continue
        while curr_range < len(fresh) and ing > fresh[curr_range][1]:
            curr_range += 1
        if curr_range != len(fresh) and fresh[curr_range][0] <= ing <= fresh[curr_range][1]:
            ans += 1
    return ans
print(solution1())

def solution2():
    merged = [fresh[0]]
    for i in range(1, len(fresh)):
        if merged[-1][1] >= fresh[i][0]:
            merged[-1][1] = max(merged[-1][1], fresh[i][1])
        else:
            merged.append(fresh[i])
    ans = 0
    for left, right in merged:
        ans += right - left + 1
    return ans
print(solution2())

