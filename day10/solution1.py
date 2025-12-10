from collections import deque
machines = []

def state_to_bin(state):
    ans = 0
    for bool in state:
        ans += bool
        ans <<= 1
    return ans >> 1

with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip('\n').split(" ")
        diagram = line[0]
        num_lights = len(diagram[1:-1])
        parsed_diagram = state_to_bin([char == '#' for char in diagram[1:-1]])
        buttons = line[1:-1]
        parsed_buttons = set()
        for button in buttons:
            controls = set(map(lambda x: int(x), button[1:-1].split(",")))
            parsed_buttons.add(state_to_bin([l in controls for l in range(num_lights)]))
        machines.append([parsed_diagram, parsed_buttons])

def part1():
    ans = 0
    for machine in machines:
        diagram, buttons = machine
        q = deque([(diagram, 1, buttons)])
        done = False
        while q and not done:
            top, count, options = q.popleft()
            for button in options:
                nxt = top ^ button
                if nxt == 0:
                    ans += count
                    done = True
                    break
                copy = options.copy()
                copy.remove(button)
                q.append((nxt, count + 1, copy))
    return ans

print(part1())
