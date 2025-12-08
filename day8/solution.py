import math
file = "input.txt"

boxes = []
with open(file, "r") as f:
    for line in f:
        line = line.rstrip('\n')
        boxes.append(list(map(lambda x: int(x), line.split(","))))
dists = []
for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        norm = sum((boxes[i][dim] - boxes[j][dim]) ** 2 for dim in range(3))
        dist = math.sqrt(norm)
        dists.append((dist, i, j))
dists.sort()

def update(sets, belongs, box1, box2):
    if belongs[box1] is None and belongs[box2] is None:
        belongs[box1] = belongs[box2] = len(sets)
        sets.append(set([box1, box2]))
    elif belongs[box1] is None:
        belongs[box1] = belongs[box2]
        sets[belongs[box1]].add(box1)
    elif belongs[box2] is None:
        belongs[box2] = belongs[box1]
        sets[belongs[box2]].add(box2)
    elif belongs[box1] != belongs[box2]:
        sets[belongs[box1]] |= sets[belongs[box2]]
        old_id = belongs[box2]
        for id in sets[belongs[box2]]:
            belongs[id] = belongs[box1]
        sets[old_id].clear()

def part1():
    CONNECTIONS = 1000 if file == "input.txt" else 10
    sets = []
    belongs = [None] * len(boxes)
    for i in range(CONNECTIONS):
        _, box1, box2 = dists[i]
        update(sets, belongs, box1, box2)
    set_lengths = [len(s) for s in sets]
    set_lengths.sort(reverse=True)
    ans = 1
    for i in range(3):
        ans *= set_lengths[i]
    return ans
print(part1())

def part2():
    sets = []
    belongs = [None] * len(boxes)
    todo = len(boxes) - 1
    prev = None

    for _, box1, box2 in dists:
        if todo == 0:
            break
        prev = (box1, box2)
        if belongs[box1] is None or belongs[box2] is None or belongs[box1] != belongs[box2]:
            todo -= 1
            update(sets, belongs, box1, box2)
    return boxes[prev[0]][0] * boxes[prev[1]][0]

print(part2())
