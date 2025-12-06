nums = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip('\n')
        try:
            nums.append(list(map(lambda x: int(x), line.split())))
        except Exception:
            signs = line.split()

ans = 0
for i in range(len(nums[0])):
    if signs[i] == '+':
        ans += sum(nums[r][i] for r in range(len(nums)))
    else:
        curr = 1
        for r in range(len(nums)):
            curr *= nums[r][i]
        ans += curr
print(ans)
