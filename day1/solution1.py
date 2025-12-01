rotations = []
with open("input.txt", "r") as f:
    for line in f:
        direction = line[0]
        magnitude = int(line[1:]) * (1 if direction == 'R' else -1)
        rotations.append(magnitude)

curr_position = 50
count = 0
for rotation in rotations:
    curr_position = (curr_position + rotation) % 100
    if curr_position == 0:
        count += 1
print(count)
