num_lines = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip('\n')
        num_lines.append(line)
sign_line = num_lines.pop()

signs = []
widths = []
curr = 0
for char in sign_line:
    if char == '+' or char == '*':
        signs.append(char)
        if curr > 0:
            widths.append(curr)
        curr = 1
    else:
        curr += 1
widths.append(curr)

nums = [[""] * (widths[i] - (0 if i == len(widths) - 1 else 1)) for i in range(len(widths))]
for row, num_line in enumerate(num_lines):
    big_i = 0
    for w, width in enumerate(widths):
        for small_i in range(width):
            if num_line[big_i + small_i] != ' ':
                nums[w][small_i] += num_line[big_i + small_i]
        big_i += width

ans = 0
for i, arg_list in enumerate(nums):
    if signs[i] == '+':
        ans += sum(map(lambda x: int(x), arg_list))
    else:
        curr = 1
        for num in arg_list:
            curr *= int(num)
        ans += curr
print(ans)
