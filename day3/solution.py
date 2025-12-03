banks = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip('\n')
        curr = [int(char) for char in line]
        banks.append(curr)

def solution1():
    ans = 0
    for bank in banks:
        first = -1
        max_i = None
        for i in range(len(bank) - 1):
            if bank[i] > first:
                max_i = i
                first = bank[i]
        second = max(bank[max_i+1:])
        ans += 10 * first + second
    return ans
print(solution1())

def digits_to_num(digits):
    ans = 0
    for digit in digits[:-1]:
        ans += digit
        ans *= 10
    ans += digits[-1]
    return ans
def solution2():
    ans = 0
    for bank in banks:
        digits = []
        curr = 0
        for battery in range(12):
            digit = -1
            max_i = None
            for i in range(curr, len(bank) - (12 - battery) + 1):
                if bank[i] > digit:
                    max_i = i
                    digit = bank[i]
            curr = max_i + 1
            digits.append(digit)
        ans += digits_to_num(digits)
    return ans
print(solution2())
