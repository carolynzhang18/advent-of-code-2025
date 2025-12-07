rotations = []
with open("input.txt", "r") as f:
    for line in f:
        direction = line[0]
        magnitude = int(line[1:]) * (1 if direction == 'R' else -1)
        rotations.append(magnitude)

def part1():
    curr_position = 50
    count = 0
    for rotation in rotations:
        curr_position = (curr_position + rotation) % 100
        if curr_position == 0:
            count += 1
    return count

def part2():
    curr_position = 50
    count = 0
    for rotation in rotations:
        # each full circle passes 0 exactly once
        full_circles = abs(rotation) // 100
        count += full_circles
        # check if leftover rotation moves position to 0 or past 0
        leftover_rotation = rotation - full_circles * (100 if rotation >= 0 else -100)
        if leftover_rotation != 0:
            next_position = curr_position + leftover_rotation
            # pointer moved to 0
            if next_position == 0 or next_position == 100:
                count += 1
            # pointer moved past 0
            elif curr_position != 0 and (next_position < 0 or next_position > 100):
                count += 1
        curr_position = (curr_position + leftover_rotation) % 100
    return count

print(part1())
print(part2())
