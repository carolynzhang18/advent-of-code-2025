from scipy.optimize import linprog
machines = []

with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip('\n').split(" ")
        joltage = line[-1]
        parsed_joltage = list(map(lambda x: int(x), joltage[1:-1].split(",")))
        num_lights = len(parsed_joltage)
        buttons = line[1:-1]
        parsed_buttons = [[0] * len(buttons) for _ in range(num_lights)]
        for i, button in enumerate(buttons):
            button = list(map(lambda x: int(x), button[1:-1].split(",")))
            for light in button:
                parsed_buttons[light][i] = 1
        machines.append([parsed_buttons, parsed_joltage])

def part2():
    ans = 0
    for machine in machines:
        buttons, joltage = machine
        ones = [1] * len(buttons[0])
        ans += linprog(c=ones, A_eq=buttons, b_eq=joltage, integrality=ones).fun
    return int(ans)

print(part2())
