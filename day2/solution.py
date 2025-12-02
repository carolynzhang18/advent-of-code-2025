ranges = []
with open("input.txt", "r") as f:
    for line in f:
        ranges_str = line.split(",")
        for range_str in ranges_str:
            left, right = range_str.split("-")
            ranges.append([left, right])

def solution1():
    ans = 0
    for left, right in ranges:
        length = 1
        factor = None # 11, 101, 1001, ...
        for num in range(int(left), int(right) + 1):
            if len(str(num)) > length:
                if len(str(num)) % 2 == 0:
                    length = len(str(num))
                    factor = int('1' + '0' * ((len(str(num)) - 2) // 2) + '1')
                else:
                    factor = None
            if factor is not None and num % factor == 0:
                ans += num
    return ans

def solution2():
    ans = 0
    for left, right in ranges:
        for num in range(int(left), int(right) + 1):
            length = len(str(num))
            for i in range(1, length // 2 + 1):
                if length % i == 0 and str(num) == str(num)[0:i] * (length // i):
                    ans += num
                    break
    return ans

print(solution1())
print(solution2())
